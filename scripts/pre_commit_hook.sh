#!/bin/bash
#
# Tracked pre-commit hook implementation for manuscript verification.
# The local .git/hooks/pre-commit hook should delegate to this script.

set -euo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

# Colors for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

resolve_python() {
    if [ -n "${PYTHON:-}" ] && [ -x "${PYTHON}" ]; then
        printf '%s\n' "${PYTHON}"
        return 0
    fi

    if [ -x "${ROOT_DIR}/.venv/bin/python" ]; then
        printf '%s\n' "${ROOT_DIR}/.venv/bin/python"
        return 0
    fi

    if command -v python3 >/dev/null 2>&1; then
        command -v python3
        return 0
    fi

    return 1
}

if ! PYTHON_BIN="$(resolve_python)"; then
    echo ""
    echo -e "${RED}❌ COMMIT BLOCKED${NC}"
    echo ""
    echo "No usable Python interpreter found for manuscript verification."
    echo "Expected one of:"
    echo "  • \$PYTHON"
    echo "  • .venv/bin/python"
    echo "  • python3 on PATH"
    echo ""
    exit 1
fi

version_check() {
    "$PYTHON_BIN" - <<'PY'
import pathlib
import sys

try:
    import yaml
except Exception:
    print("unknown")
    sys.exit(0)

root = pathlib.Path.cwd()
claims = root / "config" / "numerical_claims.yaml"
try:
    data = yaml.safe_load(claims.read_text())
    print(data["metadata"]["version"])
except Exception:
    print("unknown")
PY
}

parse_json_summary() {
    "$PYTHON_BIN" -c '
import json
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(1)

summary = data.get("summary", {})
errors = int(summary.get("errors", 0))
warnings = int(summary.get("warnings", 0))
print(f"{errors} {warnings}")
'
}

SIGNIFICANT_CHANGES="$(
    git diff --cached --name-only | awk '
        /^(analysis|config|figures|manuscript)\// { count += 1 }
        END { print count + 0 }
    '
)"
CURRENT_VERSION="$(version_check)"

if [ "${SIGNIFICANT_CHANGES}" -gt 5 ]; then
    echo ""
    echo -e "${BLUE}💡 Version Check${NC}"
    echo "   Detected ${SIGNIFICANT_CHANGES} significant file changes"
    echo "   Current version: v${CURRENT_VERSION}"
    echo ""
    echo "   Consider version bump if this represents:"
    echo "     • New analysis results"
    echo "     • Infrastructure changes"
    echo "     • Manuscript submission/revision"
    echo ""
    echo "   To update: Edit config/numerical_claims.yaml"
    echo "   Then: git tag v<new-version>"
    echo ""
fi

echo ""
echo "🔍 Running manuscript verification..."
echo ""

set +e
VERIFY_OUTPUT="$("$PYTHON_BIN" analysis/verify_manuscript_consistency.py --json 2>&1)"
VERIFY_EXIT_CODE=$?
set -e

if ! SUMMARY="$(printf '%s' "$VERIFY_OUTPUT" | parse_json_summary)"; then
    echo -e "${RED}❌ COMMIT BLOCKED${NC}"
    echo ""
    echo "Manuscript verification did not produce valid JSON output."
    echo "Interpreter: $PYTHON_BIN"
    echo "Exit code: $VERIFY_EXIT_CODE"
    echo ""
    printf '%s\n' "$VERIFY_OUTPUT"
    echo ""
    exit 1
fi

ERRORS="${SUMMARY%% *}"
WARNINGS="${SUMMARY##* }"

set +e
"$PYTHON_BIN" analysis/verify_manuscript_consistency.py
set -e

echo ""

if [ "$ERRORS" -gt 0 ]; then
    echo -e "${RED}❌ COMMIT BLOCKED${NC}"
    echo ""
    echo "Found $ERRORS error(s) in manuscript verification."
    echo "Please fix the errors before committing."
    echo ""
    echo "To see detailed output:"
    echo "  $PYTHON_BIN analysis/verify_manuscript_consistency.py"
    echo ""
    echo "To bypass this hook (NOT RECOMMENDED):"
    echo "  git commit --no-verify"
    echo ""
    exit 1
fi

if [ "$WARNINGS" -gt 0 ]; then
    echo -e "${YELLOW}⚠️  COMMIT ALLOWED WITH WARNINGS${NC}"
    echo ""
    echo "Found $WARNINGS warning(s)."
    echo "Consider fixing these before submission."
    echo ""
    exit 0
fi

echo -e "${GREEN}✅ Verification passed - proceeding with commit${NC}"
echo ""
exit 0
