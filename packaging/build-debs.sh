#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
: "${XR_SOURCE_DIR:?Set XR_SOURCE_DIR to a new external preparation directory; normal builds use xr-build-components}"
source=$(realpath -m -- "$XR_SOURCE_DIR")
workspace=$(dirname -- "$root")
case "$source" in "$workspace"|"$workspace"/*) echo "Prepared sources must be outside the canonical source workspace" >&2; exit 1;; esac
if [ -e "$source" ]; then echo "Use a new preparation directory; resume locked integration builds with xr-build-components --resume" >&2; exit 1; fi
if [ ! -d "$source/.git" ]; then
 if [ -n "${XR_UPSTREAM_REPO:-}" ]; then python3 "$root/tools/prepare-source.py" --output "$source" --upstream-repo "$XR_UPSTREAM_REPO"; else python3 "$root/tools/prepare-source.py" --output "$source"; fi
fi
cd "$source"
exec dpkg-buildpackage -us -uc -b "$@"
