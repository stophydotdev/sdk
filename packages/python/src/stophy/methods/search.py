from __future__ import annotations

from typing import List, Optional, cast

from ..transport import AsyncTransport, SyncTransport
from ..types import SearchResponse


def _payload(
    q: str,
    *,
    type: Optional[str] = None,
    sort_by: Optional[str] = None,
    upload_date: Optional[str] = None,
    duration: Optional[str] = None,
    features: Optional[List[str]] = None,
    continuation_token: Optional[str] = None,
):
    if not q.strip():
        raise ValueError("q cannot be empty")
    return {
        "q": q,
        "type": type,
        "sortBy": sort_by,
        "uploadDate": upload_date,
        "duration": duration,
        "features": features,
        "continuationToken": continuation_token,
    }


def search(transport: SyncTransport, q: str, **options) -> SearchResponse:
    return cast(SearchResponse, transport.post("/v1/search", _payload(q, **options)))


async def search_async(transport: AsyncTransport, q: str, **options) -> SearchResponse:
    return cast(SearchResponse, await transport.post("/v1/search", _payload(q, **options)))
