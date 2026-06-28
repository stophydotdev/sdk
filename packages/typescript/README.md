# stophy

Official TypeScript SDK for [Stophy](https://stophy.dev) — the **YouTube context API for AI agents**. Search videos, fetch transcripts, read comments and live chat, inspect channels and playlists, and get autocomplete suggestions, all returned as structured JSON.

Fully typed, dependency-light (built on `fetch`), works in Node, Bun, Deno, and the browser.

## Install

```bash
npm install stophy
```

Get an API key from your [Stophy dashboard](https://stophy.dev). The SDK sends it as `Authorization: Bearer <key>` on every request.

## Quick start

```ts
import { Stophy } from "stophy";

const stophy = new Stophy({ apiKey: process.env.STOPHY_API_KEY! });

const { data } = await stophy.video({
  type: "transcript",
  videoUrl: "https://www.youtube.com/watch?v=D7liwdjvhWc",
});
console.log(data?.text);
```

## Methods

| Method | Description |
| --- | --- |
| `stophy.video(body)` | Details, transcript, comments, replies, or live chat (set `type`) |
| `stophy.search(body)` | Search with filters for type, sort, date, duration, features |
| `stophy.channel(body)` | Channel metadata + content by tab (`video`/`short`/`playlist`/`about`) |
| `stophy.playlist(body)` | Playlist items, paginated |
| `stophy.suggest(query)` | Search autocomplete suggestions |
| `stophy.credits()` | Current credit balance |
| `stophy.logs(query?)` | Recent request logs |
| `stophy.usage(query?)` | Daily credit/request counts |

### Examples

```ts
// Search
const results = await stophy.search({ q: "typescript tutorial", sortBy: "popularity", duration: "long" });

// Comments (top-level), then replies to a comment.
// `video()` is overloaded on `type`, so `data` is typed — no casts needed.
const comments = await stophy.video({ type: "comments", videoUrl, sortBy: "top" });
const firstReplyToken = comments.data.items[0]?.repliesToken;
if (firstReplyToken) {
  const replies = await stophy.video({ type: "replies", continuationToken: firstReplyToken });
}

// Channel videos
const channel = await stophy.channel({ channelUrl: "https://www.youtube.com/@mkbhd", tab: "video" });

// Autocomplete
const { data: s } = await stophy.suggest({ q: "react", hl: "en", gl: "US" });
console.log(s?.suggestions);

// Account
console.log((await stophy.credits()).data?.credits);
```

### Pagination

List endpoints return a `continuationToken`. Pass it back in to fetch the next page:

```ts
let token: string | undefined;
do {
  const page = await stophy.search({ q: "lofi", continuationToken: token });
  // ...handle page.data?.items
  token = page.data?.continuationToken ?? undefined;
} while (token);
```

## Errors

Non-2xx responses throw a `StophyError`:

```ts
import { Stophy, StophyError } from "stophy";

try {
  await stophy.credits();
} catch (err) {
  if (err instanceof StophyError) {
    console.error(err.status, err.code, err.message, err.requestId);
    // err.code: "UNAUTHORIZED" | "INSUFFICIENT_CREDITS" | "BAD_REQUEST" |
    //           "INVALID_INPUT" | "NOT_FOUND" | "CONCURRENCY_LIMITED" | "INTERNAL_ERROR"
  }
}
```

## Configuration

```ts
new Stophy({
  apiKey: "sk_...",                  // required
  baseUrl: "https://api.stophy.dev", // optional override
  headers: { "x-app": "my-app" },    // optional, sent on every request
  fetch: customFetch,                // optional fetch implementation
  maxRetries: 2,                     // optional, 0 disables (default 2)
  retryInitialDelayMs: 500,          // optional backoff base (default 500)
});
```

### Retries

Transient failures — network errors and `429`/`500`/`502`/`503`/`504` — are retried automatically with exponential backoff and jitter, honoring the `Retry-After` header. Every endpoint is a read, so retries are always safe. Set `maxRetries: 0` to opt out.

Need lower-level access? The underlying [`@hey-api/client-fetch`](https://heyapi.dev) client is exposed as `stophy.client`.

## License

MIT
