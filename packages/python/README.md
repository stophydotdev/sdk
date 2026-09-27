# stophy

Official Python SDK for [Stophy](https://stophy.dev), the **web data API for AI agents**.

## Install

```bash
pip install stophy
```

Get an API key from your [Stophy dashboard](https://stophy.dev). The SDK sends it as `Authorization: Bearer <key>`.

## Quick start

```python
from stophy import Stophy

stophy = Stophy()  # reads STOPHY_API_KEY
result = stophy.youtube.search(query="bun runtime", limit=2)
print(result["data"]["results"])

markdown = stophy.youtube.search(query="bun runtime", limit=2, format="markdown")
```

`AsyncStophy` has the same methods and is awaitable. Namespaces follow the API: `POST /v1/maps/search` is `client.maps.search(query=...)`. Nested routes are nested attributes, so `client.youtube.comments.replies(video=..., cursor=...)`.

Keyword arguments are snake_case. A JSON field named `from` is passed as `from_`. `format="markdown"` sends `Accept: text/markdown` and returns a string.

```python
usage = stophy.usage()
logs = stophy.logs(days=7, page=0)
```

`usage` and `logs` call `GET /v1/usage` and `GET /v1/logs`. Both require an API key.

## Errors

```python
from stophy import StophyError

try:
    stophy.youtube.search(query="bun runtime")
except StophyError as error:
    print(error.code, error.retryable, error.retry_after_seconds)
```

`StophyError` has `code`, `retryable`, `retry_after_seconds`, `status`, and `request_id`. The message is `str(error)`.

Transient failures (network errors and HTTP 429/500/502/503/504) are retried with backoff, honoring `Retry-After`. Set `max_retries=0` to turn that off.

## Regenerating

From the repo root: `bun run sync`, then `bun run generate`. Do not edit `src/stophy/generated/`.
