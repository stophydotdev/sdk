# stophy

## 1.0.8

### Patch Changes

- 2690531: Follow the new API. Every request names things as the response does: send a link or an id, such as `videoUrl` or `videoId`, `placeUrl` or `placeId`, `userUrl` or `username`, and exactly one of the pair. `sortBy` is now `sort`, and a few filters are renamed. Search, news, images, maps, Play, flights and trends now live under `google`, and `transcript` is now `youtube.transcript`, `instagram.transcript` and `tiktok.transcript`. Amazon search, product, bestsellers and suggest are new. Page-numbered results no longer return `hasMore`: ask for the next page until `results` is empty. Most calls cost 1 credit, some cost 2, and long lists cost 1 credit per 10 results.
- 8398d41: Airbnb, Booking, company career pages, Threads, Trustpilot and eBay are new. Search stays and read a listing and its reviews with `airbnb.search`, `airbnb.listing` and `airbnb.reviews`. Search hotels and read one with `booking.search`, `booking.hotel` and `booking.hotel.reviews`. List a company's open jobs from its own job board with `careers.jobs` and `careers.job`. Read Threads with `threads.profile`, `threads.profile.posts` and `threads.post`. Check a company with `trustpilot.search`, `trustpilot.company` and `trustpilot.company.reviews`. Search eBay with `ebay.search` and `ebay.item`. Each call costs 1 credit.

## 1.0.7

### Patch Changes

- 5e54488: `limit` is gone. Each call returns one page from the site. Page-numbered methods take `page` and return `page` and `hasMore`; the others return the site's own `cursor` to pass back. `meta.ads.page` takes `advertiser`.

## 1.0.6

### Patch Changes

- b2fb8e6: Add google.search, google.news, google.images, google.shopping, google.aiMode, ai.answer, linkedin.people.search and linkedin.companies.search. web.search and web.news keep working and call the same searches.

## 1.0.5

### Patch Changes

- 305d224: Add methods and types for App Store, Google Play, Indeed, Tripadvisor and Walmart. Walmart search costs 5 credits and Walmart product 3, the rest cost 1. `transcript` costs 2 credits when the video has captions, and otherwise 2 plus 1 per 10 seconds of audio, up to 30 minutes. It now returns `transcribedSeconds` for the audio it had to transcribe.

## 1.0.4

### Patch Changes

- a28723f: Follow the API we ship. The client now covers only the endpoints the API serves, so the types and methods for the rest are gone. `tiktok.profile` and `instagram.profile` return their list in `results` and page with `limit` and `cursor`. On `instagram.profile` the post count is now `posts`, where it was `postCount`. Only web search works without a key. New input and output fields follow the API, including `mediaType` on Meta ads.

## 1.0.3

### Patch Changes

- 6166fbf: Follow the latest API. `email.verify` replaces `email.check`, `email.find` takes `domain` and an optional name, and `web.contacts` is gone. New output fields on airbnb, flights, rightmove and meta ads, `keyless` replaces `free` in search rows, and cursor paging with `limit` has no gaps.

## 1.0.2

### Patch Changes

- ce89546: Follow the flat v1 API. Responses are `{ success, data, creditsUsed, requestId }` with a flat `data`. New `transcript`, `suggest`, `ads.search`, `ads.ad`, `ads.advertisers`, `google.trends` and `finance.stock` methods; `ads.*`, `suggest` and `google.trends` take `network`, `source` and `by` with matching types. Removed the markdown `format` option and every endpoint the API no longer serves.

## 1.0.1

### Patch Changes

- 1d5bed6: New package description and keywords, and README examples for YouTube transcripts, Reddit, Google Maps reviews and Amazon products.

## 1.0.0

### Major Changes

- Every endpoint is generated from the live Stophy API. Call `stophy.youtube.search({ query })` and the same shape for every catalog endpoint.
- The old YouTube-only methods are gone: the `kids` and `music` namespaces, the hand-written YouTube methods, and `credits()`.
- The API key is optional. Without one, `web.search`, `youtube.search`, and `youtube.transcript` work on the free limit; other endpoints throw `StophyError` with code `unauthorized`.
- Errors include `retryable` and `retryAfterSeconds`. A `Retry-After` over 60 seconds throws right away instead of waiting.
- Requests time out after 30 seconds by default (`timeoutMs`) and send `User-Agent: stophy-typescript/<version>` outside browsers.
- `@hey-api/client-fetch` is no longer a runtime dependency.

## 0.3.0

### Minor Changes

- 4f9bbc4: Add YouTube Music and YouTube Kids SDK methods, switch suggestions to the POST API, and tighten response envelope/data types so stable API fields are required while upstream-variable fields remain nullable.

## 0.2.1

### Patch Changes

- 7aac084: Align generated response and request types with the API's normalized payloads, including discriminated video requests and richer search, channel, playlist, comments, and live-chat context.

## 0.2.0

### Minor Changes

- ffe672c: Add ergonomic endpoint helpers, environment-based configuration, and a modular client architecture while preserving existing object-style calls.
