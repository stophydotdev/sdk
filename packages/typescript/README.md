# stophy

Official TypeScript SDK for [Stophy](https://stophy.dev), the **web data API for AI agents**.

## Install

```bash
npm install stophy
```

Get an API key from your [Stophy dashboard](https://stophy.dev). The SDK sends it as `Authorization: Bearer <key>`.

## Try without a key

```ts
import { Stophy } from "stophy";

const result = await new Stophy().web.search({ query: "bun runtime" });
console.log(result.data.results);
```

`web.search`, `youtube.search`, and `youtube.transcript` answer without a key, with a small free limit. Other endpoints throw `StophyError` with code `unauthorized` and status 401.

## Quick start

```ts
import { Stophy } from "stophy";

const stophy = new Stophy({ apiKey: process.env.STOPHY_API_KEY });
const result = await stophy.youtube.search({ query: "bun runtime", limit: 2 });
console.log(result.data.results);

const markdown = await stophy.youtube.search(
  { query: "bun runtime", limit: 2 },
  { format: "markdown" },
);
```

`new Stophy("sk_...")` also works. `apiKey` defaults to `STOPHY_API_KEY`, and `baseUrl` defaults to `STOPHY_BASE_URL` or `https://api.stophy.dev`.

Namespaces follow the API. `POST /v1/youtube/search` is `stophy.youtube.search(input)`. `POST /v1/youtube/comments/replies` is `stophy.youtube.comments.replies(input)`. Inputs and outputs come from the OpenAPI document.

Pass `{ format: "markdown" }` to send `Accept: text/markdown` and get a string. Pass `signal` to abort the request. Each attempt times out after 30 seconds; set `timeoutMs` to change that. A timeout is not retried.

```ts
const usage = await stophy.usage();
const logs = await stophy.logs({ days: 7, page: 0 });
```

`usage` and `logs` call `GET /v1/usage` and `GET /v1/logs`. Both require an API key.

## Errors

```ts
import { StophyError } from "stophy";

try {
  await stophy.youtube.search({ query: "bun runtime" });
} catch (error) {
  if (error instanceof StophyError) {
    console.log(error.code, error.retryable, error.retryAfterSeconds);
  }
}
```

`StophyError` has `code`, `message`, `retryable`, `retryAfterSeconds`, `status`, and `requestId`.

Transient failures (network errors and HTTP 429/500/502/503/504) are retried with backoff, honoring `Retry-After`. If the API asks to wait more than 60 seconds, the SDK throws right away with `retryAfterSeconds` set. Set `maxRetries: 0` to turn retries off.

## Regenerating

From the repo root: `bun run sync`, then `bun run generate`. Do not edit `src/generated/`.
