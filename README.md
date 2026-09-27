# stophy

Official client libraries for [Stophy](https://stophy.dev), the **web data API for AI agents**. One client covers the catalog: YouTube, Reddit, Maps, the web, and the rest of `POST /v1/<source>/<endpoint>`.

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

const stophy = new Stophy({ apiKey: process.env.STOPHY_API_KEY });
const result = await stophy.youtube.search({ query: "bun runtime", limit: 2 });
console.log(result.data.results);

const markdown = await stophy.youtube.search(
  { query: "bun runtime", limit: 2 },
  { format: "markdown" },
);
```

### Python

```bash
pip install stophy
```

```python
from stophy import Stophy

stophy = Stophy(api_key="sk_...")  # or set STOPHY_API_KEY
result = stophy.youtube.search(query="bun runtime", limit=2)
print(result["data"]["results"])

markdown = stophy.youtube.search(query="bun runtime", limit=2, format="markdown")
```

Python also exports `AsyncStophy` with the same namespaces. Nested operations are nested attributes: `stophy.youtube.comments.replies(...)`.

`usage()` and `logs()` read `GET /v1/usage` and `GET /v1/logs`. Both require an API key.

## Errors

A failed response throws `StophyError` with `code`, `message`, `retryable`, `retryAfterSeconds` (`retry_after_seconds` in Python), `status`, and `requestId` (`request_id` in Python). The code and message come from `{ error: { code, message, retryable } }`. `retryAfterSeconds` comes from the body or the `Retry-After` header.

## Keeping the clients current

`openapi.json` is downloaded from the live API. Both clients are generated from it.

```bash
bun run sync       # GET https://api.stophy.dev/openapi.json
bun run generate   # TypeScript surface + Python models and namespaces
```

Set `STOPHY_OPENAPI_URL` to point `sync` at another spec. A new endpoint needs those two commands and nothing else.

## License

MIT
