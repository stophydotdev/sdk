import httpx
import pytest

from helpers import make_client
from stophy import Stophy


def test_missing_api_key_raises():
    with pytest.raises(ValueError, match="api_key"):
        Stophy("")


def test_defaults_to_production_base_url():
    client, calls = make_client({"json": {"success": True, "data": {"results": []}}})
    client.youtube.search(query="bun")
    assert str(calls[0].url).startswith("https://api.stophy.dev/")


def test_honors_custom_base_url():
    client, calls = make_client(
        {"json": {"success": True, "data": {"results": []}}},
        base_url="https://staging.stophy.dev",
    )
    client.youtube.search(query="bun")
    assert str(calls[0].url).startswith("https://staging.stophy.dev/")


def test_sends_bearer_token():
    client, calls = make_client({"json": {"success": True, "data": {"results": []}}})
    client.youtube.search(query="bun")
    assert calls[0].headers["authorization"] == "Bearer sk_test"


def test_includes_custom_headers():
    client, calls = make_client(
        {"json": {"success": True, "data": {"results": []}}},
        headers={"x-app": "my-app"},
    )
    client.youtube.search(query="bun")
    assert calls[0].headers["x-app"] == "my-app"


def test_exposes_underlying_client():
    client = Stophy("sk_test")
    assert isinstance(client.client, httpx.Client)
    client.close()


def test_works_as_context_manager():
    with make_client(
        {"json": {"balanceMicros": 1, "creditsUsed": 0, "requestCount": 0}}
    )[0] as client:
        assert client.usage()["creditsUsed"] == 0


def test_reads_api_key_and_base_url_from_environment(monkeypatch):
    monkeypatch.setenv("STOPHY_API_KEY", "sk_env")
    monkeypatch.setenv("STOPHY_BASE_URL", "https://env.stophy.dev")
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(
            200,
            json={
                "success": True,
                "data": {"results": []},
                "creditsUsed": 1,
                "requestId": "r",
            },
            request=request,
        )

    client = Stophy(transport=httpx.MockTransport(handler), max_retries=0)
    client.youtube.search(query="bun")
    assert calls[0].headers["authorization"] == "Bearer sk_env"
    assert str(calls[0].url).startswith("https://env.stophy.dev/")
    client.close()
