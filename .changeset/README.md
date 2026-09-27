# Changesets

Changesets manages releases for the TypeScript package (`stophy`).

Add a changeset for user-visible TypeScript changes:

```bash
bun run changeset
```

Python releases remain independent because Changesets does not version
`pyproject.toml`. Use `scripts/bump-version.sh python <version>` and publish the
resulting `python-v<version>` tag.

Both packages are at 1.0.0. After 1.0.0, every release is a patch bump
(`1.0.1`, `1.0.2`, …). Add a patch changeset unless Hussein explicitly asks
for a minor or major bump.
