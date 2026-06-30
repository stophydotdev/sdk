# stophy

Official TypeScript SDK for [Stophy](https://stophy.dev)  **YouTube context API for AI agents**. Search videos, fetch transcripts, read comments and live chat, inspect channels and playlists, and get autocomplete suggestions, all returned as structured JSON.


## Install

```bash
npm install stophy
```

Get an API key from your [Stophy dashboard](https://stophy.dev). The SDK sends it as `Authorization: Bearer <key>` on every request.

## Quick start

```ts
import { Stophy } from "stophy";

const stophy = new Stophy(); // reads STOPHY_API_KEY
const result = await stophy.transcript(
  "https://www.youtube.com/watch?v=D7liwdjvhWc",
);
console.log(result.data.text);
```

## Methods

| Method | Description |
| --- | --- |
| `stophy.videoDetails(url)` | Video metadata and related videos |
| `stophy.transcript(url)` | Timestamped captions and full text |
| `stophy.comments(url, options?)` | Top-level comments |
| `stophy.replies(token)` | Replies for a comment thread |
| `stophy.liveChat(url, options?)` | Live stream chat messages |
| `stophy.search(query, options?)` | Search with filters |
| `stophy.channel(url, options?)` | Channel metadata and content |
| `stophy.playlist(url, options?)` | Playlist items, paginated |
| `stophy.suggest(query, options?)` | Search autocomplete suggestions |
| `stophy.credits()` | Current credit balance |
| `stophy.logs(query?)` | Recent request logs |
| `stophy.usage(query?)` | Daily credit/request counts |

### Examples

```ts
// Search
const results = await stophy.search("typescript tutorial", {
  sortBy: "popularity",
  duration: "long",
});

// Comments (top-level), then replies to a comment.
// `video()` is overloaded on `type`, so `data` is typed - no casts needed.
const comments = await stophy.comments(videoUrl, { sortBy: "top" });
const firstReplyToken = comments.data.items[0]?.repliesToken;
if (firstReplyToken) {
  const replies = await stophy.replies(firstReplyToken);
}

// Channel videos
const channel = await stophy.channel("https://www.youtube.com/@mkbhd", {
  tab: "video",
});

// Autocomplete
const { data: s } = await stophy.suggest("react", { hl: "en", gl: "US" });
console.log(s?.suggestions);

// Account
console.log((await stophy.credits()).data?.credits);
```

### Pagination

List endpoints return a `continuationToken`. Pass it back in to fetch the next page:

```ts
let token: string | undefined;
do {
  const page = await stophy.search("lofi", { continuationToken: token });
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


## License

MIT
