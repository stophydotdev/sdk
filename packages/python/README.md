# stophy

Official Python SDK for [Stophy](https://stophy.dev) **YouTube context API for AI agents**. Search videos, fetch transcripts, read comments and live chat, inspect channels and playlists, and get autocomplete suggestions, all returned as structured JSON.


## Install

```bash
uv install stophy
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

## License

MIT
