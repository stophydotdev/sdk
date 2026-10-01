# Stophy SDKs

The web data layer for AI agents, in TypeScript and Python. Live web data as typed JSON. Search, video, social, jobs, places, property and ads behind one key, with a flat price per call. You pay only for answers that come back.

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

Both examples work without an API key. Web search is the only method that does. For everything else, get a key from the [dashboard](https://stophy.dev/dashboard).

## More data

A transcript, YouTube search, Google Maps reviews, a TikTok profile and Meta ads, in TypeScript:

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

const profile = await stophy.tiktok.profile({ profile: "tiktok", limit: 5 });
console.log(profile.data.followers, profile.data.results);

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

profile = stophy.tiktok.profile(profile="tiktok", limit=5)
print(profile["data"].get("followers"), profile["data"].get("results"))

ads = stophy.ads.search(network="meta", query="running shoes")
print(ads["data"]["results"])
```

To change the SDKs, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
