from __future__ import annotations

import asyncio

from stophy import AsyncStophy, Stophy
from stophy.generated.models import (
    AdsSearchResponse,
    TranscriptResponse,
    WebSearchResponse,
)


def sync_search() -> WebSearchResponse:
    with Stophy() as stophy:
        return stophy.web.search(query="bun runtime", page=2)


def sync_ads() -> AdsSearchResponse:
    with Stophy() as stophy:
        return stophy.ads.search(network="meta", query="shoes")


async def async_search() -> WebSearchResponse:
    async with AsyncStophy() as stophy:
        return await stophy.web.search(query="bun runtime", page=2)


async def async_transcript() -> TranscriptResponse:
    async with AsyncStophy() as stophy:
        return await stophy.transcript(video="https://youtu.be/abc")


def main() -> None:
    print(sync_search()["data"])
    print(asyncio.run(async_search())["data"])
