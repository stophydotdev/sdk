# Stophy SDKs

Live data from 40+ sites for AI agents in TypeScript and Python: web search, YouTube, Reddit, Google Maps, Amazon, jobs, real estate, ads, stocks and crypto. Every result is flat and typed.

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

A transcript, YouTube search, Google Maps reviews, an Amazon product and Meta ads, in TypeScript:

```ts
const stophy = new Stophy({ apiKey: "st_..." });

const transcript = await stophy.transcript({ video: "https://youtu.be/dQw4w9WgXcQ" });
console.log(transcript.data.text);

const videos = await stophy.youtube.search({ query: "bun runtime", limit: 5 });
console.log(videos.data.results);

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

And in Python:

```python
stophy = Stophy(api_key="st_...")

transcript = stophy.transcript(video="https://youtu.be/dQw4w9WgXcQ")
print(transcript["data"].get("text"))

videos = stophy.youtube.search(query="bun runtime", limit=5)
print(videos["data"]["results"])

places = stophy.maps.search(query="coffee", location="Austin, TX", limit=5)
place_id = places["data"]["results"][0].get("placeId")
if place_id:
    reviews = stophy.maps.reviews(place=place_id, limit=20)
    print(reviews["data"]["results"])

product = stophy.amazon.product(product="B08N5WRWNW", country="us")
print(product["data"].get("title"), product["data"].get("price"))

ads = stophy.ads.search(network="meta", query="running shoes")
print(ads["data"]["results"])
```

To change the SDKs, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
