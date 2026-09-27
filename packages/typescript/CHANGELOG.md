# stophy

## 1.0.0

### Major Changes

- Replace the YouTube-only client with namespaces generated from the live Stophy API. Call `stophy.youtube.search({ query })` and the same shape for every catalog endpoint. `credits()` is removed. Errors now include `retryable` and `retryAfterSeconds`.

## 0.3.0

### Minor Changes

- 4f9bbc4: Add YouTube Music and YouTube Kids SDK methods, switch suggestions to the POST API, and tighten response envelope/data types so stable API fields are required while upstream-variable fields remain nullable.

## 0.2.1

### Patch Changes

- 7aac084: Align generated response and request types with the API's normalized payloads, including discriminated video requests and richer search, channel, playlist, comments, and live-chat context.

## 0.2.0

### Minor Changes

- ffe672c: Add ergonomic endpoint helpers, environment-based configuration, and a modular client architecture while preserving existing object-style calls.
