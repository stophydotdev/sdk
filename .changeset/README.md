# Changesets

Changesets manages releases for the TypeScript package (`stophy`).

Add a changeset for user-visible TypeScript changes:

```bash
bun run changeset
```

Python releases remain independent because Changesets does not version
`pyproject.toml`. Use `scripts/bump-version.sh python <version>` and publish the
resulting `python-v<version>` tag.
