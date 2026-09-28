from __future__ import annotations

import asyncio

from stophy import AsyncStophy, Stophy
from stophy.generated.models import WebSearchResponse


def sync_search() -> WebSearchResponse:
    with Stophy() as stophy:
        return stophy.web.search(query="bun runtime", limit=3)


def sync_markdown() -> str:
    with Stophy() as stophy:
        return stophy.youtube.search(query="rust tutorial", format="markdown")


async def async_search() -> WebSearchResponse:
    async with AsyncStophy() as stophy:
        return await stophy.web.search(query="bun runtime", limit=3)


async def async_markdown() -> str:
    async with AsyncStophy() as stophy:
        return await stophy.youtube.search(query="rust tutorial", format="markdown")


def main() -> None:
    print(sync_search()["data"])
    print(asyncio.run(async_search())["data"])
