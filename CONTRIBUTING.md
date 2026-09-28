# Contributing

Thanks for contributing to Stophy.

## Keep the clients in sync with the API

Both clients are generated from the Stophy OpenAPI document, which is stored as `openapi.json`. To pick up new or changed endpoints, run:

```bash
bun run sync
bun run generate
```

`sync` downloads the live OpenAPI document. To read it from another server, set `STOPHY_OPENAPI_URL`. `generate` rebuilds the TypeScript methods and the Python models and methods. Do not edit `packages/typescript/src/generated/` or `packages/python/src/stophy/generated/` by hand.

## Check your change

```bash
bun run check
bun run test
```

`check` runs the linters and the type checkers for both languages. `test` runs both test suites.

## Pull requests

1. Fork the repository and create a branch for one change.
2. Include tests for behavior changes.
3. Never commit API keys, credentials, customer data, or build output.
4. In the pull request, describe the expected behavior, the change, and the commands you ran to check it.

## Issues

Use issues for bugs you can reproduce and for focused feature requests. To report a security problem, follow [SECURITY.md](./SECURITY.md) instead.
