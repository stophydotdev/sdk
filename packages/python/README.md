# stophy

Official Python SDK for [Stophy](https://stophy.dev) — the **YouTube context API for AI agents**. Search videos, fetch transcripts, read comments and live chat, inspect channels and playlists, and get autocomplete suggestions, all returned as structured JSON.

Built on [`httpx`](https://www.python-httpx.org/). Python 3.9+.

## Install

```bash
pip install stophy
# or: uv add stophy
```

Get an API key from your [Stophy dashboard](https://stophy.dev). The SDK sends it as `Authorization: Bearer <key>` on every request.

## Quick start

```python
import os
from stophy import Stophy

stophy = Stophy(os.environ["STOPHY_API_KEY"])

result = stophy.video(type="transcript", video_url="https://www.youtube.com/watch?v=D7liwdjvhWc")
print(result["data"]["text"])
```

## Methods

| Method | Description |
| --- | --- |
| `stophy.video(...)` | Details, transcript, comments, replies, or live chat (set `type`) |
| `stophy.search(...)` | Search with filters for type, sort, date, duration, features |
| `stophy.channel(...)` | Channel metadata + content by `tab` |
| `stophy.playlist(...)` | Playlist items, paginated |
| `stophy.suggest(...)` | Search autocomplete suggestions |
| `stophy.credits()` | Current credit balance |
| `stophy.logs(...)` | Recent request logs |
| `stophy.usage(...)` | Daily credit/request counts |

Arguments are keyword-only and snake_case; the SDK maps them to the API's field names for you. `video()` is overloaded on `type`, so the returned `data` is typed for the variant you asked for (transcript, comments, details, …).

```python
# Search
results = stophy.search(q="typescript tutorial", sort_by="popularity", duration="long")

# Comments, then replies to a comment
comments = stophy.video(type="comments", video_url=url, sort_by="top")
token = comments["data"]["items"][0].get("repliesToken")
if token:
    replies = stophy.video(type="replies", continuation_token=token)

# Autocomplete and account
print(stophy.suggest(q="react")["data"]["suggestions"])
print(stophy.credits()["data"]["credits"])
```

### Pagination

```python
token = None
while True:
    page = stophy.search(q="lofi", continuation_token=token)
    ...  # handle page["data"]["items"]
    token = page["data"].get("continuationToken")
    if not token:
        break
```

## Errors

Non-2xx responses raise `StophyError`:

```python
from stophy import Stophy, StophyError

try:
    stophy.credits()
except StophyError as err:
    print(err.status, err.code, err, err.request_id)
    # err.code: "UNAUTHORIZED" | "INSUFFICIENT_CREDITS" | "BAD_REQUEST" |
    #           "INVALID_INPUT" | "NOT_FOUND" | "CONCURRENCY_LIMITED" | "INTERNAL_ERROR"
```

## Configuration

```python
Stophy(
    api_key,
    base_url="https://api.stophy.dev",  # optional override
    headers={"x-app": "my-app"},          # optional, sent on every request
    timeout=30.0,                          # optional httpx timeout
    max_retries=2,                         # optional, 0 disables (default 2)
    retry_initial_delay=0.5,               # optional backoff base, seconds
)
```

### Retries

Transient failures — network errors and `429`/`500`/`502`/`503`/`504` — are retried automatically with exponential backoff and jitter, honoring the `Retry-After` header. Every endpoint is a read, so retries are always safe. Set `max_retries=0` to opt out.

The client is also a context manager (`with Stophy(...) as stophy:`) and exposes the underlying `httpx.Client` as `stophy.client`.

## License

MIT
