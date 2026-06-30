from __future__ import annotations

from typing import Optional, cast

from ..transport import AsyncTransport, SyncTransport
from ..types import CreditsResponse, LogsResponse, UsageResponse


def credits(transport: SyncTransport) -> CreditsResponse:
    return cast(CreditsResponse, transport.get("/v1/credits"))


async def credits_async(transport: AsyncTransport) -> CreditsResponse:
    return cast(CreditsResponse, await transport.get("/v1/credits"))


def logs(
    transport: SyncTransport,
    *,
    days: Optional[str] = None,
    endpoint: Optional[str] = None,
    page: Optional[int] = None,
) -> LogsResponse:
    return cast(
        LogsResponse,
        transport.get("/v1/logs", {"days": days, "endpoint": endpoint, "page": page}),
    )


async def logs_async(
    transport: AsyncTransport,
    *,
    days: Optional[str] = None,
    endpoint: Optional[str] = None,
    page: Optional[int] = None,
) -> LogsResponse:
    return cast(
        LogsResponse,
        await transport.get("/v1/logs", {"days": days, "endpoint": endpoint, "page": page}),
    )


def usage(
    transport: SyncTransport,
    *,
    days: Optional[str] = None,
    tz: Optional[str] = None,
) -> UsageResponse:
    return cast(UsageResponse, transport.get("/v1/usage", {"days": days, "tz": tz}))


async def usage_async(
    transport: AsyncTransport,
    *,
    days: Optional[str] = None,
    tz: Optional[str] = None,
) -> UsageResponse:
    return cast(
        UsageResponse,
        await transport.get("/v1/usage", {"days": days, "tz": tz}),
    )
