from helpers import body_of, make_client, ok, query_of


def test_video_posts_body_and_returns_data():
    client, calls = make_client(ok({"text": "hello world"}))
    res = client.video(type="transcript", video_url="https://youtu.be/abc")

    assert calls[0].method == "POST"
    assert calls[0].url.path == "/v1/video"
    assert body_of(calls[0]) == {
        "type": "transcript",
        "videoUrl": "https://youtu.be/abc",
    }
    assert res["data"] == {"text": "hello world"}
    assert res["requestId"] == "req_1"


def test_video_replies_flow():
    client, calls = make_client(ok({"items": []}))
    client.video(type="replies", continuation_token="TOKEN")
    assert body_of(calls[0]) == {"type": "replies", "continuationToken": "TOKEN"}


def test_transcript_helper():
    client, calls = make_client(ok({"text": "hello"}))
    result = client.transcript("https://youtu.be/abc")
    assert body_of(calls[0]) == {
        "type": "transcript",
        "videoUrl": "https://youtu.be/abc",
    }
    assert result["data"]["text"] == "hello"


def test_search_posts_filters():
    client, calls = make_client(ok({"items": [], "continuationToken": "next"}))
    res = client.search(q="lofi", sort_by="popularity", duration="long")

    assert calls[0].method == "POST"
    assert calls[0].url.path == "/v1/search"
    assert body_of(calls[0]) == {
        "q": "lofi",
        "sortBy": "popularity",
        "duration": "long",
    }
    assert res["data"]["continuationToken"] == "next"


def test_channel_posts_url_and_tab():
    client, calls = make_client(ok({"tab": "video", "items": []}))
    client.channel(channel_url="https://youtube.com/@mkbhd", tab="video")

    assert calls[0].url.path == "/v1/channel"
    assert body_of(calls[0]) == {
        "channelUrl": "https://youtube.com/@mkbhd",
        "tab": "video",
    }


def test_playlist_posts_url():
    client, calls = make_client(ok({"items": []}))
    client.playlist(playlist_url="https://youtube.com/playlist?list=PL123")

    assert calls[0].url.path == "/v1/playlist"
    assert body_of(calls[0]) == {
        "playlistUrl": "https://youtube.com/playlist?list=PL123"
    }


def test_suggest_posts_json_body():
    client, calls = make_client(ok({"suggestions": ["react", "react native"]}))
    res = client.suggest(q="react", hl="en", gl="US")

    assert calls[0].method == "POST"
    assert calls[0].url.path == "/v1/suggest"
    assert body_of(calls[0]) == {"q": "react", "hl": "en", "gl": "US"}
    assert "react native" in res["data"]["suggestions"]


def test_suggest_sends_only_required_q():
    client, calls = make_client(ok({"suggestions": []}))
    client.suggest(q="typescript")
    assert body_of(calls[0]) == {"q": "typescript"}


def test_music_posts_resource_body():
    client, calls = make_client(ok({"items": []}))
    client.music(type="search", q="lofi", search_type="song")
    assert calls[0].method == "POST"
    assert calls[0].url.path == "/v1/music"
    assert body_of(calls[0]) == {"type": "search", "q": "lofi", "searchType": "song"}


def test_kids_posts_resource_body():
    client, calls = make_client(ok({"items": []}))
    client.kids(type="search", q="science")
    assert calls[0].method == "POST"
    assert calls[0].url.path == "/v1/kids"
    assert body_of(calls[0]) == {"type": "search", "q": "science"}


def test_credits_takes_no_arguments():
    client, calls = make_client(ok({"credits": 42}))
    res = client.credits()

    assert calls[0].method == "GET"
    assert calls[0].url.path == "/v1/credits"
    assert res["data"]["credits"] == 42


def test_logs_forwards_query_filters():
    client, calls = make_client(ok({"logs": [], "total": 0}))
    client.logs(days="30", endpoint="/video", page=2)
    assert query_of(calls[0]) == {"days": "30", "endpoint": "/video", "page": "2"}


def test_usage_forwards_query_filters():
    client, calls = make_client(ok({"items": []}))
    client.usage(days="7", tz="-120")

    assert calls[0].url.path == "/v1/usage"
    assert query_of(calls[0]) == {"days": "7", "tz": "-120"}
