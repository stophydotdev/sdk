# Stophy for TypeScript

Live data from 40+ sites for AI agents in TypeScript: web search, YouTube, Reddit, Google Maps, Amazon, jobs, real estate, ads, stocks and crypto. Every method and result is typed.

## Install

```bash
npm install stophy
```

## Try it without a key

```ts
import { Stophy } from "stophy";

const result = await new Stophy().web.search({ query: "bun runtime" });
console.log(result.data.results);
```

Web search, YouTube search, and transcripts work without a key, with a small free allowance. Every other method throws a `StophyError` with the code `unauthorized`.

## Use an API key

Get a key from the [dashboard](https://stophy.dev/dashboard). Keys start with `st_`. Set it as `STOPHY_API_KEY`, or pass it in:

```ts
const stophy = new Stophy({ apiKey: "st_..." });

const videos = await stophy.youtube.search({ query: "bun runtime", limit: 5 });
console.log(videos.data.results);
```

`new Stophy("st_...")` works too.

Methods follow the source and the command: `stophy.maps.search(...)`, `stophy.reddit.subreddit(...)`, `stophy.ads.search({ network: "meta", ... })`. Endpoints with a single name are methods on the client: `stophy.transcript(...)`, `stophy.suggest(...)`.

Every response is `{ success, data, creditsUsed, requestId }`. `data` is one flat object. Lists are in `data.results`.

## More sources

A transcript, Reddit posts, Google Maps reviews, an Amazon product and Meta ads:

```ts
const stophy = new Stophy({ apiKey: "st_..." });

const transcript = await stophy.transcript({ video: "https://youtu.be/dQw4w9WgXcQ", includeTimestamps: true });
console.log(transcript.data.text, transcript.data.segments);

const posts = await stophy.reddit.search({ query: "bun runtime", sort: "top", within: "month" });
console.log(posts.data.results);

const places = await stophy.maps.search({ query: "coffee", location: "Austin, TX", limit: 5 });
const placeId = places.data.results[0]?.placeId;
if (placeId) {
  const reviews = await stophy.maps.reviews({ place: placeId, limit: 20 });
  console.log(reviews.data.results);
}

const product = await stophy.amazon.product({ product: "B08N5WRWNW", country: "us" });
console.log(product.data.title, product.data.price);

const ads = await stophy.ads.search({ network: "meta", query: "running shoes" });
console.log(ads.data.results);
```

Some endpoints cover several sources. Pick one with a field: `network` for `ads.*`, `source` for `suggest`, `by` for `google.trends`. The types follow the choice.

## Get the next page

When there are more results, `data.cursor` is set. Pass it back to get the next page:

```ts
const first = await stophy.reddit.search({ query: "bun" });
const next = await stophy.reddit.search({ query: "bun", cursor: first.data.cursor });
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
