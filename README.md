# Stophy SDKs

Get public web data in your TypeScript or Python code: search results, videos, social posts, places, products, jobs, homes, and more. Each result comes back typed, or as markdown for a model.

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

Both examples work without an API key. For every other source, get a key from the [dashboard](https://stophy.dev/dashboard).

To change the SDKs, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
