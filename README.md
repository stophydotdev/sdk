# Stophy SDKs

Live data from 40+ sites for AI agents in TypeScript and Python: web search, YouTube, Reddit, Google Maps, Amazon, jobs, real estate, ads, stocks and crypto. Each result comes back typed, or as markdown for a model.

| Language | Install | Guide |
| --- | --- | --- |
| TypeScript and JavaScript | `npm install stophy` | [packages/typescript](./packages/typescript) |
| Python | `pip install stophy` | [packages/python](./packages/python) |

```ts
import { Stophy } from "stophy";

const result = await new Stophy().web.search({ query: "bun runtime" });
```

```python
from stophy import Stophy

result = Stophy().web.search(query="bun runtime")
```

Both examples work without an API key. For every other source, get a key from the [dashboard](https://stophy.dev/dashboard).

## More sources

A YouTube transcript, Reddit posts, Google Maps reviews and an Amazon product, in TypeScript:

```ts
const stophy = new Stophy({ apiKey: "st_..." });

const transcript = await stophy.youtube.transcript({ video: "dQw4w9WgXcQ", includeTimestamps: true });
console.log(transcript.data.text, transcript.data.segments);

const posts = await stophy.reddit.search({ query: "bun runtime", sort: "top", within: "month" });
console.log(posts.data.results);

const places = await stophy.maps.search({ query: "coffee", near: "Austin, TX", limit: 5 });
const placeId = places.data.places[0]?.id;
if (placeId) {
  const reviews = await stophy.maps.reviews({ place: placeId, limit: 20 });
  console.log(reviews.data.reviews);
}

const product = await stophy.amazon.product({ product: "B08N5WRWNW", country: "us" });
console.log(product.data.product.title, product.data.product.price);
```

And in Python:

```python
stophy = Stophy(api_key="st_...")

transcript = stophy.youtube.transcript(video="dQw4w9WgXcQ", include_timestamps=True)
print(transcript["data"].get("text"), transcript["data"].get("segments"))

posts = stophy.reddit.search(query="bun runtime", sort="top", within="month")
print(posts["data"]["results"])

places = stophy.maps.search(query="coffee", near="Austin, TX", limit=5)
place_id = places["data"]["places"][0].get("id")
if place_id:
    reviews = stophy.maps.reviews(place=place_id, limit=20)
    print(reviews["data"]["reviews"])

product = stophy.amazon.product(product="B08N5WRWNW", country="us")
item = product["data"]["product"]
print(item.get("title"), item.get("price"))
```


To change the SDKs, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
