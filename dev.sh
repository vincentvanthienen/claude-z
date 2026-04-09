#!/usr/bin/env bash
# dev.sh — watch for file changes, push to GitHub, update the plugin
#
# Usage: ./dev.sh
# Stop:  Ctrl+C

PLUGIN="gen-z@gen-z"
DIR="$(cd "$(dirname "$0")" && pwd)"
INTERVAL=2

echo "Watching $(basename "$DIR") for changes..."
echo "On change: git push → claude plugin update $PLUGIN"
echo "Press Ctrl+C to stop"
echo ""

get_hash() {
  find "$DIR" \
    \( -name "*.py" -o -name "*.md" -o -name "*.json" -o -name "*.sh" \) \
    ! -path "*/.git/*" \
    -exec md5 -q {} \; 2>/dev/null | sort | md5 -q
}

last_hash=$(get_hash)

while true; do
  sleep "$INTERVAL"
  current_hash=$(get_hash)

  if [ "$current_hash" != "$last_hash" ]; then
    echo "$(date '+%H:%M:%S') change detected"

    cd "$DIR" || exit 1

    # Stage and commit changed files
    git add -A
    if git diff --cached --quiet; then
      echo "  nothing to commit (already staged?)"
    else
      git commit -m "wip: dev auto-update" --quiet
      echo "  committed"
    fi

    # Push
    if git push --quiet 2>&1; then
      echo "  pushed"
    else
      echo "  push failed — check git status"
      last_hash="$current_hash"
      continue
    fi

    # Update plugin
    if claude plugin update "$PLUGIN" 2>&1; then
      echo "  plugin updated"
    else
      echo "  plugin update failed"
    fi

    echo ""
    last_hash="$current_hash"
  fi
done
