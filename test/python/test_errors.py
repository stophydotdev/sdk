import pytest

from helpers import make_client
from stophy import StophyError


def test_error_envelope_becomes_stophy_error():
    client, _calls = make_client(
        {
            "status": 401,
            "json": {
                "success": False,
                "error": {
                    "code": "unauthorized",
                    "message": "Invalid API key",
                    "retryable": False,
                    "requestId": "req_err",
                },
            },
        }
    )
    with pytest.raises(StophyError) as info:
        client.youtube.search(query="x")
    err = info.value
    assert err.status == 401
    assert err.code == "unauthorized"
    assert str(err) == "Invalid API key"
    assert err.retryable is False
    assert err.request_id == "req_err"


def test_retry_after_comes_from_body_then_header():
    client, _calls = make_client(
        {
            "status": 429,
            "json": {
                "success": False,
                "error": {
                    "code": "rateLimited",
                    "message": "slow down",
                    "retryable": True,
                    "retryAfterSeconds": 9,
                    "requestId": "req_2",
                },
            },
        }
    )
    with pytest.raises(StophyError) as info:
        client.usage()
    assert info.value.retry_after_seconds == 9
    assert info.value.retryable is True

    client, _calls = make_client(
        {
            "status": 429,
            "headers": {"retry-after": "4", "x-request-id": "req_header"},
            "json": {
                "success": False,
                "error": {
                    "code": "rateLimited",
                    "message": "slow down",
                    "retryable": True,
                },
            },
        }
    )
    with pytest.raises(StophyError) as info:
        client.usage()
    assert info.value.retry_after_seconds == 4
    assert info.value.request_id == "req_header"


def test_non_json_error_uses_the_status():
    client, _calls = make_client({"status": 502, "raw": "bad gateway"})
    with pytest.raises(StophyError) as info:
        client.usage()
    assert info.value.status == 502
    assert "502" in str(info.value)
    assert info.value.retryable is True


def test_success_does_not_raise():
    client, _calls = make_client(
        {"json": {"balanceMicros": 1, "creditsUsed": 0, "requestCount": 0}}
    )
    assert client.usage()["requestCount"] == 0
