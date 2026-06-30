import pytest

from stophy import StophyError
from helpers import make_client


def test_raises_on_401_with_code_and_message():
    client, _ = make_client(
        {
            "status": 401,
            "json": {
                "success": False,
                "code": "UNAUTHORIZED",
                "error": "Invalid API key",
            },
        }
    )
    with pytest.raises(StophyError) as info:
        client.credits()
    err = info.value
    assert err.status == 401
    assert err.code == "UNAUTHORIZED"
    assert str(err) == "Invalid API key"


def test_maps_insufficient_credits_402():
    client, _ = make_client(
        {
            "status": 402,
            "json": {
                "success": False,
                "code": "INSUFFICIENT_CREDITS",
                "error": "Out of credits",
            },
        }
    )
    with pytest.raises(StophyError) as info:
        client.search(q="x")
    assert info.value.status == 402
    assert info.value.code == "INSUFFICIENT_CREDITS"


def test_surfaces_validation_details_400():
    client, _ = make_client(
        {
            "status": 400,
            "json": {
                "success": False,
                "code": "INVALID_INPUT",
                "error": "videoUrl is required",
                "details": {"field": "videoUrl"},
            },
        }
    )
    with pytest.raises(StophyError) as info:
        client.video(type="details", video_url="")
    assert info.value.code == "INVALID_INPUT"
    assert info.value.details == {"field": "videoUrl"}


def test_captures_request_id_header():
    client, _ = make_client(
        {
            "status": 500,
            "headers": {"x-request-id": "req_err_99"},
            "json": {"success": False, "code": "INTERNAL_ERROR", "error": "boom"},
        }
    )
    with pytest.raises(StophyError) as info:
        client.credits()
    assert info.value.request_id == "req_err_99"


def test_falls_back_to_status_message_on_non_json():
    client, _ = make_client({"status": 429, "raw": "Too Many Requests"})
    with pytest.raises(StophyError) as info:
        client.credits()
    assert info.value.status == 429
    assert "429" in str(info.value)


def test_success_does_not_raise():
    client, _ = make_client({"json": {"success": True, "data": {"credits": 5}}})
    assert client.credits()["data"]["credits"] == 5
