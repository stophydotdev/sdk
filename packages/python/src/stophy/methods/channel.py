from __future__ import annotations

from typing import Optional, cast

from ..transport import AsyncTransport, SyncTransport
from ..types import ChannelResponse


def _payload(
    channel_url: str,
    *,
    query: Optional[str] = None,
    tab: Optional[str] = None,
    sort_by: Optional[str] = None,
    continuation_token: Optional[str] = None,
):
    return {
        "channelUrl": channel_url,
        "query": query,
        "tab": tab,
        "sortBy": sort_by,
        "continuationToken": continuation_token,
    }


def channel(transport: SyncTransport, channel_url: str, **options) -> ChannelResponse:
    return cast(
        ChannelResponse,
        transport.post("/v1/channel", _payload(channel_url, **options)),
    )


async def channel_async(transport: AsyncTransport, channel_url: str, **options) -> ChannelResponse:
    return cast(
        ChannelResponse,
        await transport.post("/v1/channel", _payload(channel_url, **options)),
    )
