from __future__ import annotations

from typing import Optional, cast

from ..transport import AsyncTransport, SyncTransport
from ..types import PlaylistResponse


def _payload(playlist_url: str, *, continuation_token: Optional[str] = None):
    return {
        "playlistUrl": playlist_url,
        "continuationToken": continuation_token,
    }


def playlist(transport: SyncTransport, playlist_url: str, **options) -> PlaylistResponse:
    return cast(
        PlaylistResponse,
        transport.post("/v1/playlist", _payload(playlist_url, **options)),
    )


async def playlist_async(
    transport: AsyncTransport, playlist_url: str, **options
) -> PlaylistResponse:
    return cast(
        PlaylistResponse,
        await transport.post("/v1/playlist", _payload(playlist_url, **options)),
    )
