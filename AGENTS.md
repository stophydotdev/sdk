# Stophy SDKs

This repo ships two clients for the Stophy API: `packages/typescript` (npm `stophy`) and `packages/python` (PyPI `stophy`). Both are generated from `openapi.json`, so both have the same methods: `stophy.youtube.search(...)`, `stophy.youtube.comments.replies(...)`, and so on, plus `usage()` and `logs()`.

## Generated and hand-written code

Never edit these folders by hand. `bun run generate` overwrites them.

- `packages/typescript/src/generated/`
- `packages/python/src/stophy/generated/`

To change a method, change the API, then sync and regenerate. To change how every call behaves, edit the hand-written files:

| Behavior | TypeScript (`packages/typescript/src/`) | Python (`packages/python/src/stophy/`) |
| --- | --- | --- |
| Client and options | `client.ts`, `bind.ts` | `client.py`, `client_async.py` |
| HTTP, retries, timeouts | `transport.ts` | `transport.py` |
| Errors | `errors.ts` | `errors.py` |
| `usage()` and `logs()` | `account.ts` | `account.py` |

## Commands

Run these from the repo root.

```bash
bun run sync       # download the live openapi.json
bun run generate   # regenerate both clients
bun run check      # lint and type-check both languages
bun run test       # run both test suites
```

After `sync`, check `git diff openapi.json` before you regenerate. A new endpoint needs only `sync` and `generate`. The TypeScript test "exposes every operation in the spec" covers it.

Tests in `test/typescript` and `test/python` use a mock server. They never call the real API and need no key. Keep the two helpers, `test/typescript/helpers.ts` and `test/python/helpers.py`, in step.

Python supports 3.9 and later. Keep `from __future__ import annotations` at the top of each source file.

## Commits

Work on a branch. Use Conventional Commits with a scope: `typescript`, `python`, or `root` (spec, scripts, CI, repo files). Example: `fix(python): read Retry-After in seconds`.

## Releases

Merging never publishes. Both packages are at 1.0.0, and every later release is a patch: 1.0.1, 1.0.2, and so on. Ask Hussein before a minor or major bump.

- TypeScript: add a patch changeset with `bun run changeset`. Merge the feature PR, then merge the `version package` PR that Changesets opens.
- Python: set the version with `scripts/bump-version.sh python <version>` in a normal PR.
- Publish by hand: `gh workflow run publish.yml -R stophydotdev/sdk -f package=typescript` (or `python`, or `both`). The workflow skips a version that is already published. It logs in to npm and PyPI with trusted publishing, so do not add a publish token.
