from __future__ import annotations

import os
from typing import Any, Mapping

import httpx

from .account import Logs, Usage, parse_logs, parse_usage
from .generated.namespaces import SyncSurface
from .transport import DEFAULT_BASE_URL, SyncTransport, compact, default_headers


class Stophy(SyncSurface):
    """Synchronous client for the Stophy web scraping API."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float = 30.0,
        max_retries: int = 2,
        retry_initial_delay: float = 0.5,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        resolved_key = (api_key or os.getenv("STOPHY_API_KEY", "")).strip()
        resolved_url = base_url or os.getenv("STOPHY_BASE_URL") or DEFAULT_BASE_URL
        self.client = httpx.Client(
            base_url=resolved_url,
            headers=default_headers(resolved_key, headers),
            timeout=timeout,
            transport=transport,
        )
        self._transport = SyncTransport(
            self.client,
            max_retries=max_retries,
            retry_initial_delay=retry_initial_delay,
        )
        super().__init__(self._request)

    def _request(
        self,
        method: str,
        path: str,
        body: Mapping[str, Any] | None,
    ) -> Any:
        if method == "GET":
            return self._transport.request(method, path)
        return self._transport.request(method, path, json={} if body is None else body)

    def usage(self) -> Usage:
        """Current balance and lifetime usage. Requires an API key."""
        return parse_usage(self._transport.get("/v1/usage"))

    def logs(
        self,
        *,
        days: int | None = None,
        page: int | None = None,
        api_key_id: str | None = None,
        endpoint: str | None = None,
    ) -> Logs:
        """Recent metered requests. Requires an API key."""
        return parse_logs(
            self._transport.get(
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

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> Stophy:
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()
