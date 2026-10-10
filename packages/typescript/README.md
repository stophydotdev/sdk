# Stophy for TypeScript

Web scraping API for AI agents, in TypeScript. One API to search the web, read what people say, and look up products, places, jobs and homes. Pay only for answers. Every method and result is typed.

## Install

```bash
npm install stophy
```

## Try it without a key

```ts
import { Stophy } from "stophy";

const result = await new Stophy().google.search({ query: "bun runtime" });
console.log(result.data.results);
```

Some searches and lookups work without a key, within a small free allowance. The [endpoint list](https://api.stophy.dev/v1/endpoints) marks them with `keyless: true`. Every other method throws a `StophyError` with the code `unauthorized`.

## Use an API key

Get a key from the [dashboard](https://stophy.dev/dashboard). Keys start with `st_`. Set it as `STOPHY_API_KEY`, or pass it in:

```ts
const stophy = new Stophy({ apiKey: "st_..." });

const videos = await stophy.youtube.search({ query: "bun runtime" });
console.log(videos.data.results);
```

`new Stophy("st_...")` works too.

Methods follow the source and the command: `stophy.google.maps.search(...)`, `stophy.reddit.subreddit(...)`, `stophy.meta.ads.search(...)`.

To point at one thing, send its link or its id, never both: `stophy.youtube.video({ videoUrl })` or `stophy.youtube.video({ videoId })`. Methods that take a person send `userUrl` or `username`.

Every response is `{ success, data, creditsUsed, requestId }`. `data` is one flat object. Lists are in `data.results`.

## More data

A YouTube transcript, Reddit posts, Google Maps reviews, a TikTok profile and Meta ads:

```ts
const stophy = new Stophy({ apiKey: "st_..." });

const transcript = await stophy.youtube.transcript({ videoUrl: "https://youtu.be/dQw4w9WgXcQ", includeTimestamps: true });
console.log(transcript.data.text, transcript.data.segments);

const posts = await stophy.reddit.search({ query: "bun runtime", sort: "top", within: "month" });
console.log(posts.data.results);

const places = await stophy.google.maps.search({ query: "coffee", location: "Austin, TX" });
const placeId = places.data.results[0]?.placeId;
if (placeId) {
  const reviews = await stophy.google.maps.reviews({ placeId });
  console.log(reviews.data.results);
}

const profile = await stophy.tiktok.profile({ username: "tiktok" });
console.log(profile.data.followers, profile.data.results);

const ads = await stophy.meta.ads.search({ query: "running shoes" });
console.log(ads.data.results);
```

## Get the next page

Each call returns one page of results, as the site shows it. List methods page in one of two ways.

Some take a page number. They return `data.page`. Ask for the next number to continue, and stop when `results` comes back empty:

```ts
const first = await stophy.google.search({ query: "bun runtime" });
const second = await stophy.google.search({ query: "bun runtime", page: first.data.page + 1 });
```

Others return `data.cursor` when there is more. Pass it back as is:

```ts
const first = await stophy.youtube.search({ query: "bun runtime" });
if (first.data.cursor) {
  const next = await stophy.youtube.search({ query: "bun runtime", cursor: first.data.cursor });
}
```

## Handle errors

```ts
import { StophyError } from "stophy";

try {
  await stophy.reddit.search({ query: "bun" });
} catch (error) {
  if (error instanceof StophyError) {
    console.log(error.code, error.retryable, error.retryAfterSeconds);
  }
}
```

`StophyError` has `code`, `message`, `retryable`, `retryAfterSeconds`, `status`, and `requestId`.

The SDK retries network errors and the HTTP statuses 429, 500, 502, 503, and 504, and it waits as long as the API asks. If the API asks for a wait longer than 60 seconds, the SDK throws right away with `retryAfterSeconds` set.

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `apiKey` | `STOPHY_API_KEY` | Your API key |
| `baseUrl` | `STOPHY_BASE_URL`, or the Stophy API | The server to call |
| `maxRetries` | `2` | Retries per request. `0` turns retries off. |
| `timeoutMs` | `30000` | Time limit for each attempt. A timed-out attempt is not retried. |

Each method also takes `signal` to cancel the request.

## Check your account

```ts
const usage = await stophy.usage();
const logs = await stophy.logs({ days: 7, page: 0 });
```

`usage` returns your balance and your all-time usage. `logs` returns your recent requests. Both need an API key.

## License

MIT
