import asyncio

import httpx
import pytest

from helpers import body_of
from stophy import AsyncStophy, StophyError


def _run(function):
    return asyncio.run(function())


def test_async_search_and_markdown():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        if request.headers.get("accept") == "text/markdown":
            return httpx.Response(200, text="# results", request=request)
        return httpx.Response(
            200,
            json={
                "success": True,
                "data": {"results": [{"url": "https://youtu.be/abc"}]},
                "creditsUsed": 1,
                "requestId": "req_1",
            },
            request=request,
        )

    async def run():
        async with AsyncStophy(
            "sk_test",
            transport=httpx.MockTransport(handler),
            max_retries=0,
        ) as client:
            result = await client.youtube.search(query="bun runtime", limit=2)
            text = await client.youtube.search(query="bun runtime", format="markdown")
            return result, text

    result, text = _run(run)
    assert result["data"]["results"][0]["url"] == "https://youtu.be/abc"
    assert text == "# results"
    assert body_of(calls[0]) == {"query": "bun runtime", "limit": 2}
    assert calls[1].headers["accept"] == "text/markdown"


def test_async_error_has_code():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            401,
            json={
                "success": False,
                "error": {
                    "code": "unauthorized",
                    "message": "nope",
                    "retryable": False,
                    "requestId": "req_a",
                },
            },
            request=request,
        )

    async def run():
        async with AsyncStophy(
            "sk_test",
            transport=httpx.MockTransport(handler),
            max_retries=0,
        ) as client:
            await client.youtube.search(query="x")

    with pytest.raises(StophyError) as info:
        _run(run)
    assert info.value.code == "unauthorized"
    assert info.value.request_id == "req_a"


def test_async_client_reads_environment(monkeypatch):
    monkeypatch.setenv("STOPHY_API_KEY", "sk_env")
    monkeypatch.setenv("STOPHY_BASE_URL", "https://env.stophy.dev")

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["authorization"] == "Bearer sk_env"
        assert request.url.host == "env.stophy.dev"
        return httpx.Response(
            200,
            json={"balanceMicros": 1, "creditsUsed": 0, "requestCount": 0},
            request=request,
        )

    async def run():
        async with AsyncStophy(
            transport=httpx.MockTransport(handler), max_retries=0
        ) as client:
            usage = await client.usage()
            assert usage["balanceMicros"] == 1

    _run(run)


def test_async_raises_instead_of_waiting_more_than_60_seconds():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(
            429,
            headers={"retry-after": "120"},
            json={"success": False, "error": {"code": "rateLimited"}},
            request=request,
        )

    async def run():
        async with AsyncStophy(
            "sk_test",
            transport=httpx.MockTransport(handler),
            max_retries=2,
            retry_initial_delay=0,
        ) as client:
            await client.youtube.search(query="x")

    with pytest.raises(StophyError) as info:
        _run(run)
    assert info.value.retry_after_seconds == 120
    assert len(calls) == 1
