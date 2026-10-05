# Stophy SDKs

The web data layer for AI agents, in TypeScript and Python. Live web data as typed JSON. Search, video, social, jobs, places, property and ads behind one key, with a price shown before every call. You pay only for answers that come back.

| Language | Install | Guide |
| --- | --- | --- |
| TypeScript and JavaScript | `npm install stophy` | [packages/typescript](./packages/typescript) |
| Python | `pip install stophy` | [packages/python](./packages/python) |

```ts
import { Stophy } from "stophy";

const result = await new Stophy().google.search({ query: "bun runtime" });
```

```python
from stophy import Stophy

result = Stophy().google.search(query="bun runtime")
```

Both examples work without an API key. So do Google News, YouTube search, YouTube video details, YouTube transcripts, Reddit search and Google Maps search, within a small free allowance. For everything else, get a key from the [dashboard](https://stophy.dev/dashboard).

## More data

A transcript, YouTube search, Google Maps reviews, a TikTok profile and Meta ads, in TypeScript:

```ts
const stophy = new Stophy({ apiKey: "st_..." });

const transcript = await stophy.youtube.transcript({ videoUrl: "https://youtu.be/dQw4w9WgXcQ" });
console.log(transcript.data.text);

const videos = await stophy.youtube.search({ query: "bun runtime" });
console.log(videos.data.results);

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

And in Python:

```python
stophy = Stophy(api_key="st_...")

transcript = stophy.youtube.transcript(video_url="https://youtu.be/dQw4w9WgXcQ")
print(transcript["data"].get("text"))

videos = stophy.youtube.search(query="bun runtime")
print(videos["data"]["results"])

places = stophy.google.maps.search(query="coffee", location="Austin, TX")
place_id = places["data"]["results"][0].get("placeId")
if place_id:
    reviews = stophy.google.maps.reviews(place_id=place_id)
    print(reviews["data"]["results"])

profile = stophy.tiktok.profile(username="tiktok")
print(profile["data"].get("followers"), profile["data"].get("results"))

ads = stophy.meta.ads.search(query="running shoes")
print(ads["data"]["results"])
```

To change the SDKs, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
