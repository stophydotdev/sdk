---
"stophy": major
---

The client follows the live API. Web scrape, parse, map, contacts, crawl and batch, web images, Glassdoor company reviews and salaries, Yelp search, business and reviews, Amazon reviews, and X profile posts are new. `web.search` and `web.news` now call their own endpoints: `web.search` takes `limit` and `scrapeResults` instead of `page`, and `web.news` no longer takes `topic`, `language` or `page`. `google.news` takes `page` up to 10. The endpoints the API removed are gone, so `google.aiMode`, `google.shopping` and `google.jobs` no longer have methods.
