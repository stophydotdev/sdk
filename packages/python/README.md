# Stophy for Python

The web data layer for AI agents, in Python. Live web data as typed JSON. Search, video, social, jobs, places, property and ads behind one key, with a price shown before every call. You pay only for answers that come back. Every method and result is typed.

## Install

```bash
pip install stophy
```

## Try it without a key

```python
from stophy import Stophy

result = Stophy().google.search(query="bun runtime")
print(result["data"]["results"])
```

Web search works without a key, with a small free allowance. Every other method raises a `StophyError` with the code `unauthorized`.

## Use an API key

Get a key from the [dashboard](https://stophy.dev/dashboard). Keys start with `st_`. Set it as `STOPHY_API_KEY`, or pass it in:

```python
stophy = Stophy(api_key="st_...")

videos = stophy.youtube.search(query="bun runtime")
print(videos["data"]["results"])
```

Methods follow the source and the command: `stophy.maps.search(...)`, `stophy.reddit.subreddit(...)`, `stophy.ads.search(network="meta", ...)`. Endpoints with a single name are methods on the client, like `stophy.transcript(...)`.

Every response is a dict with `success`, `data`, `creditsUsed`, and `requestId`. `data` is one flat dict. Lists are in `data["results"]`.

Arguments are keyword-only and snake_case.

For async code, use `AsyncStophy`. It has the same methods, and you `await` each call.

## More data

A transcript, Reddit posts, Google Maps reviews, a TikTok profile and Meta ads:

```python
stophy = Stophy(api_key="st_...")

transcript = stophy.transcript(video="https://youtu.be/dQw4w9WgXcQ", include_timestamps=True)
print(transcript["data"].get("text"), transcript["data"].get("segments"))

posts = stophy.reddit.search(query="bun runtime", sort="top", within="month")
print(posts["data"]["results"])

places = stophy.maps.search(query="coffee", location="Austin, TX")
place_id = places["data"]["results"][0].get("placeId")
if place_id:
    reviews = stophy.maps.reviews(place=place_id)
    print(reviews["data"]["results"])

profile = stophy.tiktok.profile(profile="tiktok")
print(profile["data"].get("followers"), profile["data"].get("results"))

ads = stophy.ads.search(network="meta", query="running shoes")
print(ads["data"]["results"])
```

`ads.search` covers several ad networks. Pick one with `network`. The type checker follows the choice.

## Get the next page

Each call returns one page of results, as the site shows it. List methods page in one of two ways.

Some take a page number. They return `data["page"]` and `data["hasMore"]`. Ask for the next number while `hasMore` is true:

```python
first = stophy.google.search(query="bun runtime")
if first["data"].get("hasMore"):
    second = stophy.google.search(query="bun runtime", page=2)
```

Others return `data["cursor"]` when there is more. Pass it back as is:

```python
first = stophy.youtube.search(query="bun runtime")
if first["data"].get("cursor"):
    next_page = stophy.youtube.search(query="bun runtime", cursor=first["data"]["cursor"])
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
