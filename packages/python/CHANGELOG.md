# stophy

## 1.0.1

- New package description and keywords, and README examples for YouTube transcripts, Reddit, Google Maps reviews and Amazon products.

## 1.0.0

- Every endpoint is generated from the live Stophy API. Call `stophy.youtube.search(query=...)` and the same shape for every catalog endpoint, on `Stophy` and `AsyncStophy`.
- The old YouTube-only methods are gone: the `kids` and `music` namespaces, the hand-written YouTube methods, and `credits()`.
- The API key is optional. Without one, `web.search`, `youtube.search`, and `youtube.transcript` work on the free limit; other endpoints raise `StophyError` with code `unauthorized`.
- Errors include `retryable` and `retry_after_seconds`. A `Retry-After` over 60 seconds raises right away instead of waiting.
- Requests send `User-Agent: stophy-python/<version>`.
