---
"stophy": patch
---

Follow the API we ship. The client now covers only the endpoints the API serves, so the types and methods for the rest are gone. `tiktok.profile` and `instagram.profile` return their list in `results` and page with `limit` and `cursor`. On `instagram.profile` the post count is now `posts`, where it was `postCount`. Only web search works without a key. New input and output fields follow the API, including `mediaType` on Meta ads.
