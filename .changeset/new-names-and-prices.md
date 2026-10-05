---
"stophy": patch
---

Follow the new API. Every request names things as the response does: send a link or an id, such as `videoUrl` or `videoId`, `placeUrl` or `placeId`, `userUrl` or `username`, and exactly one of the pair. `sortBy` is now `sort`, and a few filters are renamed. Search, news, images, maps, Play, flights and trends now live under `google`, and `transcript` is now `youtube.transcript`, `instagram.transcript` and `tiktok.transcript`. Amazon search, product, bestsellers and suggest are new. Page-numbered results no longer return `hasMore`: ask for the next page until `results` is empty. Most calls cost 1 credit, some cost 2, and long lists cost 1 credit per 10 results.
