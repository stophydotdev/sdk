from __future__ import annotations

import os
from typing import Any, Mapping

import httpx

from .account import Logs, Usage, parse_logs, parse_usage
from .generated.namespaces import AsyncSurface
from .transport import DEFAULT_BASE_URL, AsyncTransport, compact, default_headers


class AsyncStophy(AsyncSurface):
    """Asynchronous client for the Stophy web data API."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float = 30.0,
        max_retries: int = 2,
        retry_initial_delay: float = 0.5,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        resolved_key = (api_key or os.getenv("STOPHY_API_KEY", "")).strip()
        resolved_url = base_url or os.getenv("STOPHY_BASE_URL") or DEFAULT_BASE_URL
        self.client = httpx.AsyncClient(
            base_url=resolved_url,
            headers=default_headers(resolved_key, headers),
            timeout=timeout,
            transport=transport,
        )
        self._transport = AsyncTransport(
            self.client,
            max_retries=max_retries,
            retry_initial_delay=retry_initial_delay,
        )
        super().__init__(self._request)

    async def _request(
        self,
        method: str,
        path: str,
        body: Mapping[str, Any] | None,
        format: str | None,
    ) -> Any:
        headers = {"Accept": "text/markdown" if format == "markdown" else "application/json"}
        if method == "GET":
            return await self._transport.request(method, path, headers=headers)
        return await self._transport.request(
            method, path, headers=headers, json={} if body is None else body
        )

    async def usage(self) -> Usage:
        """Current balance and lifetime usage. Requires an API key."""
        return parse_usage(await self._transport.get("/v1/usage"))

    async def logs(
        self,
        *,
        days: int | None = None,
        page: int | None = None,
        api_key_id: str | None = None,
        endpoint: str | None = None,
    ) -> Logs:
        """Recent metered requests. Requires an API key."""
        return parse_logs(
            await self._transport.get(
                "/v1/logs",
                compact(
                    {
                        "days": days,
                        "page": page,
                        "apiKeyId": api_key_id,
                        "endpoint": endpoint,
                    }
                ),
            )
        )

    async def close(self) -> None:
        await self.client.aclose()

    async def __aenter__(self) -> AsyncStophy:
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.close()
