import json
from pathlib import Path

from helpers import body_of, make_client, query_of

ENVELOPE = {
    "success": True,
    "data": {
        "results": [
            {
                "type": "video",
                "videoId": "abc",
                "videoUrl": "https://youtu.be/abc",
                "channelName": "Bun",
            }
        ]
    },
    "creditsUsed": 1,
    "requestId": "req_1",
}


def test_posts_input_to_the_spec_path():
    client, calls = make_client({"json": ENVELOPE})
    result = client.youtube.search(query="bun runtime", limit=2)
    assert result["data"]["results"][0]["videoUrl"] == "https://youtu.be/abc"
    assert calls[0].method == "POST"
    assert calls[0].url.path == "/v1/youtube/search"
    assert body_of(calls[0]) == {"query": "bun runtime", "limit": 2}
    assert calls[0].headers["accept"] == "application/json"


def test_single_segment_operations_and_keyword_argument():
    client, calls = make_client({"json": ENVELOPE})
    client.transcript(video="https://youtu.be/abc", include_timestamps=True)
    assert calls[0].url.path == "/v1/transcript"
    assert body_of(calls[0]) == {
        "video": "https://youtu.be/abc",
        "includeTimestamps": True,
    }

    client.suggest(source="google", query="bun")
    assert calls[1].url.path == "/v1/suggest"
    assert body_of(calls[1]) == {"source": "google", "query": "bun"}

    client.finance.history(symbol="AAPL", from_="2026-01-01")
    assert body_of(calls[2])["from"] == "2026-01-01"


def test_joined_operations_send_the_discriminator():
    client, calls = make_client({"json": ENVELOPE})
    client.ads.search(network="meta", query="shoes")
    client.google.trends(by="time", queries=["bun"])
    assert calls[0].url.path == "/v1/ads/search"
    assert body_of(calls[0]) == {"network": "meta", "query": "shoes"}
    assert calls[1].url.path == "/v1/google/trends"
    assert body_of(calls[1]) == {"by": "time", "queries": ["bun"]}


def test_empty_optional_body_and_endpoint_catalog():
    client, calls = make_client(
        [{"json": ENVELOPE}, {"json": {"endpoints": []}}],
    )
    client.crypto.coins()
    catalog = client.endpoints()
    assert body_of(calls[0]) == {}
    assert calls[0].url.path == "/v1/crypto/coins"
    assert catalog["endpoints"] == []
    assert calls[1].method == "GET"


def test_usage_and_logs():
    client, calls = make_client(
        [
            {"json": {"balanceMicros": 1000, "creditsUsed": 2, "requestCount": 1}},
            {
                "json": {
                    "endpoints": ["youtube.search"],
                    "logs": [
                        {
                            "apiKeyId": None,
                            "apiKeyName": None,
                            "createdAt": "2026-09-28T00:00:00.000Z",
                            "credits": 1,
                            "durationMs": None,
                            "endpoint": "youtube.search",
                            "id": "log_1",
                            "method": "POST",
                            "response": "success",
                            "status": 200,
                        }
                    ],
                    "page": 0,
                    "pageSize": 50,
                    "total": 1,
                    "totalPages": 1,
                }
            },
        ]
    )
    assert client.usage()["creditsUsed"] == 2
    logs = client.logs(days=7, page=0, endpoint="youtube.search", api_key_id="key_1")
    assert logs["logs"][0]["endpoint"] == "youtube.search"
    assert query_of(calls[1]) == {
        "days": "7",
        "page": "0",
        "endpoint": "youtube.search",
        "apiKeyId": "key_1",
    }


def test_every_spec_operation_is_callable():
    spec = json.loads(Path("openapi.json").read_text())
    client, _calls = make_client({"json": ENVELOPE})
    assert len(spec["paths"]) > 90
    for path in spec["paths"]:
        node = client
        for part in [item for item in path.split("/") if item and item != "v1"]:
            node = getattr(node, part)
        assert callable(node)
    client.close()
