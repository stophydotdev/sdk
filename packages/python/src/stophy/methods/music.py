from __future__ import annotations

from typing import Optional, cast

from ..transport import AsyncTransport, SyncTransport
from ..types import MusicResponse


def _payload(
    *,
    type: str,
    q: Optional[str] = None,
    search_type: Optional[str] = None,
    video_url: Optional[str] = None,
    album_url: Optional[str] = None,
    artist_url: Optional[str] = None,
    playlist_url: Optional[str] = None,
    continuation_token: Optional[str] = None,
):
    required = {
        "search": ("q", q),
        "suggest": ("q", q),
        "song": ("video_url", video_url),
        "lyrics": ("video_url", video_url),
        "album": ("album_url", album_url),
        "artist": ("artist_url", artist_url),
        "playlist": ("playlist_url", playlist_url),
    }
    if type not in required:
        raise ValueError(f"unsupported music type: {type}")
    name, value = required[type]
    if not value or not value.strip():
        raise ValueError(f"{name} is required when type is {type}")
    return {
        "type": type,
        "q": q,
        "searchType": search_type,
        "videoUrl": video_url,
        "albumUrl": album_url,
        "artistUrl": artist_url,
        "playlistUrl": playlist_url,
        "continuationToken": continuation_token,
    }


def music(transport: SyncTransport, **options) -> MusicResponse:
    return cast(MusicResponse, transport.post("/v1/music", _payload(**options)))


async def music_async(transport: AsyncTransport, **options) -> MusicResponse:
    return cast(MusicResponse, await transport.post("/v1/music", _payload(**options)))
