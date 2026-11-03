#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-user}"
PROJECT_DIR="${2:-$PWD}"
FORCE=""

case "$MODE" in
  user)
    DEST="$HOME/.agents/skills"
    FORCE="${2:-}"
    ;;
  project)
    DEST="$PROJECT_DIR/.agents/skills"
    FORCE="${3:-}"
    ;;
  *) echo "Usage: $0 [user [--force] | project /path/to/project [--force]]" >&2; exit 2 ;;
esac

if [[ "$FORCE" != "" && "$FORCE" != "--force" ]]; then
  echo "The optional force argument must be --force." >&2
  exit 2
fi
mkdir -p "$DEST"
installed=0
skipped=0
for source in skills/*; do
  [[ -d "$source" ]] || continue
  name="$(basename "$source")"
  target="$DEST/$name"
  if [[ -e "$target" && "$FORCE" != "--force" ]]; then
    echo "Skipping existing skill: $name (pass --force to replace)"
    skipped=$((skipped+1))
    continue
  fi
  if [[ -e "$target" ]]; then rm -rf -- "$target"; fi
  cp -R -- "$source" "$target"
  installed=$((installed+1))
done

echo "Installed: $installed; skipped: $skipped; destination: $DEST"
echo "In Codex, run /skills or invoke a skill with \$skill-name."
