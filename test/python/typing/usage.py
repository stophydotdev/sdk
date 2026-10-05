from __future__ import annotations

import asyncio

from stophy import AsyncStophy, Stophy
from stophy.generated.models import (
    GoogleSearchResponse,
    MetaAdsPageResponse,
    YoutubeTranscriptResponse,
)


def sync_search() -> GoogleSearchResponse:
    with Stophy() as stophy:
        return stophy.web.search(query="bun runtime", page=2)


def sync_ads() -> MetaAdsPageResponse:
    with Stophy() as stophy:
        return stophy.meta.ads.search(query="shoes")


async def async_search() -> GoogleSearchResponse:
    async with AsyncStophy() as stophy:
        return await stophy.web.search(query="bun runtime", page=2)


async def async_transcript() -> YoutubeTranscriptResponse:
    async with AsyncStophy() as stophy:
        return await stophy.youtube.transcript(video_url="https://youtu.be/abc")


def main() -> None:
    print(sync_search()["data"])
    print(asyncio.run(async_search())["data"])
