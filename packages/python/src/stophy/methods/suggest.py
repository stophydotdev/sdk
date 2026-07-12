from __future__ import annotations

from typing import Optional, cast

from ..transport import AsyncTransport, SyncTransport
from ..types import SuggestResponse


def _payload(q: str, *, hl: Optional[str] = None, gl: Optional[str] = None):
    if not q.strip():
        raise ValueError("q cannot be empty")
    return {"q": q, "hl": hl, "gl": gl}


def suggest(transport: SyncTransport, q: str, **options) -> SuggestResponse:
    return cast(SuggestResponse, transport.post("/v1/suggest", _payload(q, **options)))


async def suggest_async(transport: AsyncTransport, q: str, **options) -> SuggestResponse:
    return cast(SuggestResponse, await transport.post("/v1/suggest", _payload(q, **options)))
