---
"stophy": patch
---

`limit` is gone. Each call returns one page from the site. Page-numbered methods take `page` and return `page` and `hasMore`; the others return the site's own `cursor` to pass back. `meta.ads.page` takes `advertiser`.
