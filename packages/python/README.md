# Stophy for Python

Get public web data in your Python code: search results, videos, social posts, places, products, jobs, homes, and more. Every method and result is typed.

## Install

```bash
pip install stophy
```

## Try it without a key

```python
from stophy import Stophy

result = Stophy().web.search(query="bun runtime")
print(result["data"]["results"])
```

Web search, YouTube search, and YouTube transcripts work without a key, with a small free allowance. Every other method raises a `StophyError` with the code `unauthorized`.

## Use an API key

Get a key from the [dashboard](https://stophy.dev/dashboard). Keys start with `st_`. Set it as `STOPHY_API_KEY`, or pass it in:

```python
stophy = Stophy(api_key="st_...")

videos = stophy.youtube.search(query="bun runtime", limit=5)
print(videos["data"]["results"])
```

Methods follow the source and the command: `stophy.maps.search(...)`, `stophy.reddit.subreddit(...)`, `stophy.youtube.comments.replies(...)`. Each result has `data`, `creditsUsed`, and `requestId`.

Arguments are keyword-only and snake_case. A field named `from` is passed as `from_`.

For async code, use `AsyncStophy`. It has the same methods, and you `await` each call.

## Get markdown for a model

```python
markdown = stophy.youtube.search(query="bun runtime", limit=5, format="markdown")
```

With `format="markdown"`, the method returns a string.

## Get the next page

When there are more results, `data["cursor"]` is set. Pass it back to get the next page:

```python
first = stophy.reddit.search(query="bun")
next_page = stophy.reddit.search(query="bun", cursor=first["data"]["cursor"])
```

## Handle errors

```python
from stophy import StophyError

try:
    stophy.reddit.search(query="bun")
except StophyError as error:
    print(error.code, error.retryable, error.retry_after_seconds)
```

`StophyError` has `code`, `retryable`, `retry_after_seconds`, `status`, and `request_id`. The message is `str(error)`.

The SDK retries network errors and the HTTP statuses 429, 500, 502, 503, and 504, and it waits as long as the API asks. If the API asks for a wait longer than 60 seconds, the SDK raises right away with `retry_after_seconds` set.

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `api_key` | `STOPHY_API_KEY` | Your API key |
| `base_url` | `STOPHY_BASE_URL`, or the Stophy API | The server to call |
| `max_retries` | `2` | Retries per request. `0` turns retries off. |
| `timeout` | `30.0` | Time limit in seconds for each attempt |

## Check your account

```python
usage = stophy.usage()
logs = stophy.logs(days=7, page=0)
```

`usage` returns your balance and your all-time usage. `logs` returns your recent requests. Both need an API key.

## License

MIT
