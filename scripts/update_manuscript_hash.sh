#!/bin/bash
# Helper script to update manuscript_hash in numerical_claims.yaml to current HEAD
# Usage: ./update_manuscript_hash.sh

set -e

YAML_FILE="config/numerical_claims.yaml"

# Get current HEAD hash
CURRENT_HASH=$(git rev-parse HEAD)
SHORT_HASH=$(git rev-parse --short HEAD)

echo "📝 Updating manuscript_hash in $YAML_FILE"
echo "   Current HEAD: $SHORT_HASH"

# Update the hash using Python
python3 << EOF
import yaml

# Read the YAML file
with open('$YAML_FILE', 'r') as f:
    data = yaml.safe_load(f)

# Update metadata hash
old_hash = data['metadata']['manuscript_hash']
data['metadata']['manuscript_hash'] = '$CURRENT_HASH'

# Update version history commit (short hash) for latest version
if data['version_history'] and len(data['version_history']) > 0:
    data['version_history'][0]['commit'] = '$SHORT_HASH'

# Write back to file preserving structure
with open('$YAML_FILE', 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

print(f"   Old hash: {old_hash[:7] if len(old_hash) > 7 else old_hash}")
print(f"   New hash: $SHORT_HASH")
EOF

# Stage the change
git add "$YAML_FILE"

echo ""
echo "✅ Hash updated in $YAML_FILE"
echo ""
echo "Next steps:"
echo "  1. Review the change: git diff --staged"
echo "  2. Commit: git commit -m 'Update manuscript hash to $SHORT_HASH'"
echo "  3. Push: git push"
