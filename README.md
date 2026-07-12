# stophy

Official client libraries for [Stophy](https://stophy.dev) - the **YouTube context API for AI agents**. Search videos, fetch transcripts, read comments and live chat, inspect channels and playlists, use YouTube Music and YouTube Kids, and get autocomplete suggestions, all returned as structured JSON.

Pick your language:

- [TypeScript / JavaScript](./packages/typescript) - `npm install stophy`
- [Python](./packages/python) - `pip install stophy`

Get an API key from your [Stophy dashboard](https://stophy.dev). The SDK sends it as `Authorization: Bearer <key>` on every request.

## Quick start

### TypeScript

```bash
npm install stophy
```

```ts
import { Stophy } from "stophy";

const stophy = new Stophy(); // reads STOPHY_API_KEY
const result = await stophy.transcript(
  "https://www.youtube.com/watch?v=D7liwdjvhWc",
);
console.log(result.data.text);
```

### Python

```bash
pip install stophy
```

```python
from stophy import Stophy

stophy = Stophy()  # reads STOPHY_API_KEY
result = stophy.transcript(
    "https://www.youtube.com/watch?v=D7liwdjvhWc"
)
print(result["data"]["text"])
```

## What you can do

| Method | Description |
| --- | --- |
| `video_details(...)` / `videoDetails(...)` | Video metadata and related videos |
| `transcript(...)` | Timestamped captions and full text |
| `comments(...)` / `replies(...)` | Top-level comments and reply threads |
| `live_chat(...)` / `liveChat(...)` | Live stream chat messages |
| `search(...)` | Search with filters for type, sort, date, duration, features |
| `channel(...)` | Channel metadata + content by `tab` |
| `playlist(...)` | Playlist items, paginated |
| `suggest(...)` | Search autocomplete suggestions |
| `music(...)` | YouTube Music search, suggestions, songs, lyrics, albums, artists, playlists |
| `kids(...)` | YouTube Kids search and video metadata |
| `credits()` | Current credit balance |
| `logs(...)` | Recent request logs |
| `usage(...)` | Daily credit/request counts |

Each SDK exposes the same surface with idiomatic naming for its language (camelCase in TypeScript, snake_case in Python). Python also exports `AsyncStophy` with matching awaitable methods. The generic `video(...)` method remains available for callers that prefer the API discriminant directly.

## Errors

Non-2xx responses surface a `StophyError` with the HTTP `status`, an API `code` (`UNAUTHORIZED`, `INSUFFICIENT_CREDITS`, `BAD_REQUEST`, `INVALID_INPUT`, `NOT_FOUND`, `CONCURRENCY_LIMITED`, `INTERNAL_ERROR`), the message, and a `requestId` you can quote to support.

## Retries

Transient failures - network errors and `429`/`500`/`502`/`503`/`504` - are retried automatically with exponential backoff and jitter, honoring the `Retry-After` header. Every endpoint is a read, so retries are always safe. Both SDKs let you set `maxRetries` (TS) / `max_retries` (Python) to opt out.

## License

MIT
