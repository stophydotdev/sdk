from __future__ import annotations

import asyncio
import random
import time
from email.utils import parsedate_to_datetime
from typing import Any, Dict, Mapping, Optional

import httpx

from .errors import StophyError

DEFAULT_BASE_URL = "https://api.stophy.dev"
RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def compact(values: Mapping[str, Any]) -> Dict[str, Any]:
    return {key: value for key, value in values.items() if value is not None}


def handle_response(response: httpx.Response) -> Dict[str, Any]:
    try:
        payload = response.json()
    except ValueError:
        payload = None

    if response.is_success and isinstance(payload, dict):
        return payload

    error = payload if isinstance(payload, dict) else {}
    raise StophyError(
        error.get("error") or f"Stophy request failed with status {response.status_code}",
        status=response.status_code,
        code=error.get("code"),
        request_id=response.headers.get("x-request-id"),
        details=error.get("details"),
    )


class _RetryConfig:
    def __init__(self, max_retries: int, retry_initial_delay: float) -> None:
        self.max_retries = max_retries
        self.retry_initial_delay = retry_initial_delay

    def backoff(self, attempt: int) -> float:
        window = self.retry_initial_delay * (2**attempt)
        return window / 2 + random.random() * (window / 2)

    def retry_after(self, response: httpx.Response, attempt: int) -> float:
        header = response.headers.get("retry-after")
        if header:
            try:
                return float(header)
            except ValueError:
                try:
                    return max(0.0, parsedate_to_datetime(header).timestamp() - time.time())
                except (TypeError, ValueError):
                    pass
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

    def request(self, method: str, path: str, **kwargs: Any) -> Dict[str, Any]:
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

    def get(self, path: str, params: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        return self.request("GET", path, params=compact(params or {}))

    def post(self, path: str, body: Mapping[str, Any]) -> Dict[str, Any]:
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

    async def request(self, method: str, path: str, **kwargs: Any) -> Dict[str, Any]:
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

    async def get(self, path: str, params: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        return await self.request("GET", path, params=compact(params or {}))

    async def post(self, path: str, body: Mapping[str, Any]) -> Dict[str, Any]:
        return await self.request("POST", path, json=compact(body))
