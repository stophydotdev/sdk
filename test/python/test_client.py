import httpx
import pytest

from stophy import Stophy
from helpers import make_client


def test_missing_api_key_raises():
    with pytest.raises(ValueError, match="api_key"):
        Stophy("")


def test_defaults_to_production_base_url():
    client, calls = make_client({"json": {"success": True, "data": {}}})
    client.credits()
    assert str(calls[0].url).startswith("https://api.stophy.dev/")


def test_honors_custom_base_url():
    client, calls = make_client(
        {"json": {"success": True, "data": {}}}, base_url="https://staging.stophy.dev"
    )
    client.credits()
    assert str(calls[0].url).startswith("https://staging.stophy.dev/")


def test_sends_bearer_token():
    client, calls = make_client({"json": {"success": True, "data": {}}})
    client.credits()
    assert calls[0].headers["authorization"] == "Bearer sk_test"


def test_includes_custom_headers():
    client, calls = make_client(
        {"json": {"success": True, "data": {}}}, headers={"x-app": "my-app"}
    )
    client.credits()
    assert calls[0].headers["x-app"] == "my-app"


def test_exposes_underlying_client():
    client = Stophy("sk_test")
    assert isinstance(client.client, httpx.Client)


def test_works_as_context_manager():
    with make_client({"json": {"success": True, "data": {}}})[0] as client:
        assert client.credits()["success"] is True


def test_reads_api_key_and_base_url_from_environment(monkeypatch):
    monkeypatch.setenv("STOPHY_API_KEY", "sk_env")
    monkeypatch.setenv("STOPHY_BASE_URL", "https://env.stophy.dev")
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(200, json={"success": True, "data": {}}, request=request)

    client = Stophy(transport=httpx.MockTransport(handler), max_retries=0)
    client.credits()
    assert calls[0].url.host == "env.stophy.dev"
    assert calls[0].headers["authorization"] == "Bearer sk_env"
