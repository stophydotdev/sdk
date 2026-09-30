---
"stophy": patch
---

Follow the flat v1 API. Responses are `{ success, data, creditsUsed, requestId }` with a flat `data`. New `transcript`, `suggest`, `ads.search`, `ads.ad`, `ads.advertisers`, `google.trends` and `finance.stock` methods; `ads.*`, `suggest` and `google.trends` take `network`, `source` and `by` with matching types. Removed the markdown `format` option and every endpoint the API no longer serves.
