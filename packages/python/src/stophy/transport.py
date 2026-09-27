from __future__ import annotations

import asyncio
import random
import time
from email.utils import parsedate_to_datetime
from typing import Any, Mapping

import httpx

from .errors import StophyError

DEFAULT_BASE_URL = "https://api.stophy.dev"
RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def compact(values: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in values.items() if value is not None}


def _error_object(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return {}
    error = payload.get("error")
    if not isinstance(error, dict):
        return {}
    return error


def _header_retry_after(response: httpx.Response) -> int | None:
    header = response.headers.get("retry-after")
    if not header:
        return None
    try:
        return int(float(header))
    except ValueError:
        try:
            return max(0, int(parsedate_to_datetime(header).timestamp() - time.time()))
        except (TypeError, ValueError, OSError):
            return None


def handle_response(response: httpx.Response) -> Any:
    accept = response.request.headers.get("accept", "")
    if response.is_success and "text/markdown" in accept:
        return response.text

    try:
        payload = response.json()
    except ValueError:
        payload = None

    if response.is_success and isinstance(payload, dict):
        return payload

    error = _error_object(payload)
    message = error.get("message")
    if not isinstance(message, str) or not message:
        message = f"Stophy request failed with status {response.status_code}"
    code = error.get("code")
    retryable = error.get("retryable")
    retry_after = error.get("retryAfterSeconds")
    request_id = error.get("requestId")
    if isinstance(retry_after, bool) or not isinstance(retry_after, int):
        retry_after = _header_retry_after(response)
    if not isinstance(request_id, str):
        request_id = response.headers.get("x-request-id")
    raise StophyError(
        message,
        status=response.status_code,
        code=code if isinstance(code, str) else None,
        retryable=retryable
        if isinstance(retryable, bool)
        else response.status_code in RETRYABLE_STATUS,
        retry_after_seconds=retry_after,
        request_id=request_id,
    )


class _RetryConfig:
    def __init__(self, max_retries: int, retry_initial_delay: float) -> None:
        self.max_retries = max_retries
        self.retry_initial_delay = retry_initial_delay

    def backoff(self, attempt: int) -> float:
        window = self.retry_initial_delay * (2**attempt)
        return window / 2 + random.random() * (window / 2)

    def retry_after(self, response: httpx.Response, attempt: int) -> float:
        seconds = _header_retry_after(response)
        if seconds is not None:
            return float(seconds)
        return self.backoff(attempt)


class SyncTransport(_RetryConfig):
    def __init__(
        self,
        client: httpx.Client,
        *,
        max_retries: int,
        retry_initial_delay: float,
    ) -> None:
        super().__init__(max_retries, retry_initial_delay)
        self.client = client

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        attempt = 0
        while True:
            try:
                response = self.client.request(method, path, **kwargs)
            except httpx.TransportError:
                if attempt >= self.max_retries:
                    raise
                time.sleep(self.backoff(attempt))
                attempt += 1
                continue
            if attempt < self.max_retries and response.status_code in RETRYABLE_STATUS:
                time.sleep(self.retry_after(response, attempt))
                attempt += 1
                continue
            return handle_response(response)

    def get(self, path: str, params: Mapping[str, Any] | None = None) -> Any:
        return self.request("GET", path, params=compact(params or {}))

    def post(self, path: str, body: Mapping[str, Any]) -> Any:
        return self.request("POST", path, json=compact(body))


class AsyncTransport(_RetryConfig):
    def __init__(
        self,
        client: httpx.AsyncClient,
        *,
        max_retries: int,
        retry_initial_delay: float,
    ) -> None:
        super().__init__(max_retries, retry_initial_delay)
        self.client = client

    async def request(self, method: str, path: str, **kwargs: Any) -> Any:
        attempt = 0
        while True:
            try:
                response = await self.client.request(method, path, **kwargs)
            except httpx.TransportError:
                if attempt >= self.max_retries:
                    raise
                await asyncio.sleep(self.backoff(attempt))
                attempt += 1
                continue
            if attempt < self.max_retries and response.status_code in RETRYABLE_STATUS:
                await asyncio.sleep(self.retry_after(response, attempt))
                attempt += 1
                continue
            return handle_response(response)

    async def get(self, path: str, params: Mapping[str, Any] | None = None) -> Any:
        return await self.request("GET", path, params=compact(params or {}))

    async def post(self, path: str, body: Mapping[str, Any]) -> Any:
        return await self.request("POST", path, json=compact(body))
