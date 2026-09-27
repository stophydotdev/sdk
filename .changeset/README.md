# Changesets

Changesets manages releases for the TypeScript package (`stophy`).

Add a changeset for user-visible TypeScript changes:

```bash
bun run changeset
```

Python versions are set with `scripts/bump-version.sh python <version>`
because Changesets does not version `pyproject.toml`.

Merging never publishes. Release by hand:
`gh workflow run publish.yml -R stophydotdev/sdk -f package=typescript|python|both`.

Both packages are at 1.0.0. After 1.0.0, every release is a patch bump
(`1.0.1`, `1.0.2`, …). Add a patch changeset unless Hussein explicitly asks
for a minor or major bump.
