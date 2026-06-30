#!/usr/bin/env bash
# bump-version.sh — bump a package version and print the commit + tag commands.
#
# Usage:
#   ./scripts/bump-version.sh python 0.2.0
#
# TypeScript versions are normally managed by Changesets. This script remains
# available for Python releases, where it updates pyproject.toml, uv.lock, and
# the runtime __version__ value together.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  echo "Usage: $0 <package> <version>"
  echo ""
  echo "  package   python"
  echo "  version   e.g. 1.2.3  (no leading 'v')"
  echo ""
  echo "Examples:"
  echo "  $0 python 0.2.0"
  exit 1
}

[[ $# -eq 2 ]] || usage

PACKAGE="$1"
VERSION="$2"

# Validate version looks like semver (digits and dots only for simplicity)
if ! [[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[a-zA-Z0-9.]+)?$ ]]; then
  echo "Error: version must be semver, e.g. 1.2.3 or 1.2.3-beta.1"
  exit 1
fi

case "$PACKAGE" in
  python)
    INIT_FILE="$REPO_ROOT/packages/python/src/stophy/__init__.py"
    uv version --project "$REPO_ROOT/packages/python" "$VERSION" --no-sync
    sed -i "s/^__version__ = \".*\"/__version__ = \"$VERSION\"/" "$INIT_FILE"
    echo ""
    echo "Bumped Python SDK to $VERSION."
    echo ""
    echo "Next steps:"
    echo "  git add packages/python/pyproject.toml packages/python/uv.lock packages/python/src/stophy/__init__.py"
    echo "  git commit -m \"chore(python): bump version to $VERSION\""
    echo "  git tag python-v$VERSION"
    echo "  git push origin main python-v$VERSION"
    ;;
  *)
    echo "Error: unknown package '$PACKAGE'. Valid value: python"
    usage
    ;;
esac
