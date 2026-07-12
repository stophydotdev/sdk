# stophy

Official Python SDK for [Stophy](https://stophy.dev) **YouTube context API for AI agents**. Search videos, fetch transcripts, read comments and live chat, inspect channels and playlists, use YouTube Music and YouTube Kids, and get autocomplete suggestions, all returned as structured JSON.


## Install

```bash
pip install stophy
```

Get an API key from your [Stophy dashboard](https://stophy.dev). The SDK sends it as `Authorization: Bearer <key>` on every request.

## Quick start

```python
from stophy import Stophy

stophy = Stophy()  # reads STOPHY_API_KEY
result = stophy.transcript("https://www.youtube.com/watch?v=D7liwdjvhWc")
print(result["data"]["text"])
```

## Methods

| Method | Description |
| --- | --- |
| `stophy.video_details(url)` | Video metadata and related videos |
| `stophy.transcript(url)` | Timestamped captions and full text |
| `stophy.comments(url, ...)` | Top-level comments |
| `stophy.replies(token)` | Replies for a comment thread |
| `stophy.live_chat(url, ...)` | Live stream chat messages |
| `stophy.search(...)` | Search with filters for type, sort, date, duration, features |
| `stophy.channel(...)` | Channel metadata + content by `tab` |
| `stophy.playlist(...)` | Playlist items, paginated |
| `stophy.suggest(...)` | Search autocomplete suggestions |
| `stophy.music(...)` | YouTube Music search, suggestions, songs, lyrics, albums, artists, playlists |
| `stophy.kids(...)` | YouTube Kids search and video metadata |
| `stophy.credits()` | Current credit balance |
| `stophy.logs(...)` | Recent request logs |
| `stophy.usage(...)` | Daily credit/request counts |

Methods use snake_case options and map them to API field names. The generic `video(...)` method remains available for discriminant-based calls.

```python
# Search
results = stophy.search("typescript tutorial", sort_by="popularity", duration="long")

# Comments, then replies to a comment
comments = stophy.comments(url, sort_by="top")
token = comments["data"]["items"][0].get("repliesToken")
if token:
    replies = stophy.replies(token)

# Autocomplete and account
print(stophy.suggest("react")["data"]["suggestions"])
print(stophy.credits()["data"]["credits"])

# YouTube Music and YouTube Kids
music = stophy.music(type="search", q="lofi", search_type="song")
kids = stophy.kids(type="search", q="science")
print(music["data"]["items"])
print(kids["data"]["items"])
```

### Pagination

```python
token = None
while True:
    page = stophy.search("lofi", continuation_token=token)
    ...  # handle page["data"]["items"]
    token = page["data"].get("continuationToken")
    if not token:
        break
```

### Async

`AsyncStophy` exposes the same operations with `async`/`await`:

```python
from stophy import AsyncStophy

async with AsyncStophy() as stophy:
    result = await stophy.transcript(
        "https://www.youtube.com/watch?v=D7liwdjvhWc"
    )
    print(result["data"]["text"])
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
