from __future__ import annotations

from typing import Optional, cast

from ..transport import AsyncTransport, SyncTransport
from ..types import KidsResponse


def _payload(
    *,
    type: str,
    q: Optional[str] = None,
    video_url: Optional[str] = None,
    continuation_token: Optional[str] = None,
):
    if type == "search":
        if not q or not q.strip():
            raise ValueError("q is required when type is search")
    elif type == "video":
        if not video_url or not video_url.strip():
            raise ValueError("video_url is required when type is video")
    else:
        raise ValueError(f"unsupported kids type: {type}")
    return {
        "type": type,
        "q": q,
        "videoUrl": video_url,
        "continuationToken": continuation_token,
    }


def kids(transport: SyncTransport, **options) -> KidsResponse:
    return cast(KidsResponse, transport.post("/v1/kids", _payload(**options)))


async def kids_async(transport: AsyncTransport, **options) -> KidsResponse:
    return cast(KidsResponse, await transport.post("/v1/kids", _payload(**options)))
