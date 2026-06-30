import asyncio

import httpx

from stophy import AsyncStophy


def test_async_client_supports_context_manager_and_helpers():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(
            200,
            json={"success": True, "data": {"text": "hello"}},
            request=request,
        )

    async def run():
        async with AsyncStophy(
            "sk_test",
            transport=httpx.MockTransport(handler),
            max_retries=0,
        ) as client:
            result = await client.transcript("https://youtu.be/abc")
            assert result["data"]["text"] == "hello"

    asyncio.run(run())
    assert calls[0].url.path == "/v1/video"
    assert calls[0].read() == b'{"type":"transcript","videoUrl":"https://youtu.be/abc"}'


def test_async_client_reads_environment(monkeypatch):
    monkeypatch.setenv("STOPHY_API_KEY", "sk_env")
    monkeypatch.setenv("STOPHY_BASE_URL", "https://env.stophy.dev")

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["authorization"] == "Bearer sk_env"
        assert request.url.host == "env.stophy.dev"
        return httpx.Response(200, json={"success": True, "data": {}}, request=request)

    async def run():
        client = AsyncStophy(transport=httpx.MockTransport(handler), max_retries=0)
        try:
            await client.credits()
        finally:
            await client.close()

    asyncio.run(run())
