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
