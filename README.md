# stophy

Official client libraries for [Stophy](https://stophy.dev) — the **YouTube context API for AI agents**. Search videos, fetch transcripts, read comments and live chat, inspect channels and playlists, and get autocomplete suggestions, all returned as structured JSON.

Pick your language:

- [TypeScript / JavaScript](./packages/typescript) — `npm install stophy`
- [Python](./packages/python) — `pip install stophy`

Get an API key from your [Stophy dashboard](https://stophy.dev). The SDK sends it as `Authorization: Bearer <key>` on every request.

## Quick start

### TypeScript

```bash
npm install stophy
```

```ts
import { Stophy } from "stophy";

const stophy = new Stophy({ apiKey: process.env.STOPHY_API_KEY! });

const { data } = await stophy.video({
  type: "transcript",
  videoUrl: "https://www.youtube.com/watch?v=D7liwdjvhWc",
});
console.log(data?.text);
```

### Python

```bash
pip install stophy
```

```python
import os
from stophy import Stophy

stophy = Stophy(os.environ["STOPHY_API_KEY"])

result = stophy.video(
    type="transcript",
    video_url="https://www.youtube.com/watch?v=D7liwdjvhWc",
)
print(result["data"]["text"])
```

## What you can do

| Method | Description |
| --- | --- |
| `video(...)` | Details, transcript, comments, replies, or live chat (set `type`) |
| `search(...)` | Search with filters for type, sort, date, duration, features |
| `channel(...)` | Channel metadata + content by `tab` |
| `playlist(...)` | Playlist items, paginated |
| `suggest(...)` | Search autocomplete suggestions |
| `credits()` | Current credit balance |
| `logs(...)` | Recent request logs |
| `usage(...)` | Daily credit/request counts |

Each SDK exposes the same surface with idiomatic naming for its language (camelCase in TS, snake_case in Python). List endpoints return a `continuationToken` — pass it back to fetch the next page.

## Errors

Non-2xx responses surface a `StophyError` with the HTTP `status`, an API `code` (`UNAUTHORIZED`, `INSUFFICIENT_CREDITS`, `BAD_REQUEST`, `INVALID_INPUT`, `NOT_FOUND`, `CONCURRENCY_LIMITED`, `INTERNAL_ERROR`), the message, and a `requestId` you can quote to support.

## Retries

Transient failures — network errors and `429`/`500`/`502`/`503`/`504` — are retried automatically with exponential backoff and jitter, honoring the `Retry-After` header. Every endpoint is a read, so retries are always safe. Both SDKs let you set `maxRetries` (TS) / `max_retries` (Python) to opt out.

## License

MIT
