#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOOK_PATH="${ROOT_DIR}/.git/hooks/pre-commit"

mkdir -p "$(dirname "$HOOK_PATH")"

cat > "$HOOK_PATH" <<'EOF'
#!/bin/bash

set -euo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel)"
HOOK_SCRIPT="${ROOT_DIR}/scripts/pre_commit_hook.sh"

if [ ! -x "$HOOK_SCRIPT" ]; then
    echo "Missing executable hook implementation: $HOOK_SCRIPT" >&2
    exit 1
fi

exec "$HOOK_SCRIPT"
EOF

chmod +x "$HOOK_PATH"

echo "Installed pre-commit hook wrapper at $HOOK_PATH"
echo "Hook implementation: ${ROOT_DIR}/scripts/pre_commit_hook.sh"
