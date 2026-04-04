#!/bin/bash
# Prepare manuscript for Overleaf upload
# Creates zip file with correct structure and path fixes
# Version is dynamically loaded from config/numerical_claims.yaml

set -e

if [ -x ".venv/bin/python" ]; then
    PYTHON=".venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON="$(command -v python3)"
else
    echo "❌ Error: python3 not found"
    exit 1
fi

# Extract version from YAML (single source of truth)
VERSION=$("$PYTHON" -c "import yaml; data = yaml.safe_load(open('config/numerical_claims.yaml')); print(data['metadata']['version'])")
VERSION_DESC=$("$PYTHON" -c "import yaml; data = yaml.safe_load(open('config/numerical_claims.yaml')); print(data['version_history'][0]['description'])")

echo "=========================================="
echo "Distance Ladder Manuscript - Overleaf Prep"
echo "Version: v${VERSION}"
echo "=========================================="
echo ""

# Check we're in correct directory
if [ ! -f "manuscript/manuscript.tex" ]; then
    echo "❌ Error: Run this script from distance-ladder-systematics/ directory"
    exit 1
fi

# Create temporary directory for Overleaf structure
TEMP_DIR="overleaf_temp"
rm -rf "$TEMP_DIR"
mkdir -p "$TEMP_DIR"

echo "1. Copying files to temporary directory..."

# Copy manuscript files
mkdir -p "$TEMP_DIR/manuscript"
cp manuscript/manuscript.tex "$TEMP_DIR/manuscript/"
cp manuscript/references.bib "$TEMP_DIR/manuscript/"

# Copy AASTeX class file if it exists
if [ -f "manuscript/aastex701.cls" ]; then
    cp manuscript/aastex701.cls "$TEMP_DIR/manuscript/"
    echo "   ✓ Included aastex701.cls"
fi

# Copy figures (updated list with correlation heatmap)
mkdir -p "$TEMP_DIR/figures"
cp figures/figure1_tension_evolution.png "$TEMP_DIR/figures/"
cp figures/figure2_error_budget.png "$TEMP_DIR/figures/"
cp figures/figure3_cchp_crossval_real.png "$TEMP_DIR/figures/"
cp figures/figure4_h0_compilation.png "$TEMP_DIR/figures/"
cp figures/figure5_h6_fit.png "$TEMP_DIR/figures/"
cp figures/figure_correlation_heatmap.png "$TEMP_DIR/figures/"
cp figures/sensitivity_correlation.png "$TEMP_DIR/figures/"
cp figures/figure_2d_correlation_sensitivity.png "$TEMP_DIR/figures/"
cp figures/posterior_joint_delta_H0.png "$TEMP_DIR/figures/"
cp figures/corner_joint_bias_fit.png "$TEMP_DIR/figures/"

# Copy tables into data/tables/ to match manuscript include paths
mkdir -p "$TEMP_DIR/data/tables"
cp data/tables/table1_systematic_budget.tex "$TEMP_DIR/data/tables/"
cp data/tables/table2_tension_evolution.tex "$TEMP_DIR/data/tables/"
cp data/tables/table3_h0_compilation.tex "$TEMP_DIR/data/tables/"
cp data/tables/table4_cchp_crossval.tex "$TEMP_DIR/data/tables/"
cp data/tables/table_correlation_matrix.tex "$TEMP_DIR/data/tables/"

# Copy optional tables if they exist
[ -f "data/tables/table5_jwst_crossvalidation.tex" ] && cp data/tables/table5_jwst_crossvalidation.tex "$TEMP_DIR/data/tables/" || echo "   ℹ️  Skipping table5 (not found)"
[ -f "data/tables/table6_cosmic_chronometers.tex" ] && cp data/tables/table6_cosmic_chronometers.tex "$TEMP_DIR/data/tables/" || echo "   ℹ️  Skipping table6 (not found)"
[ -f "data/tables/table_anchor_weights.tex" ] && cp data/tables/table_anchor_weights.tex "$TEMP_DIR/data/tables/" || echo "   ℹ️  Skipping anchor_weights (not found)"

echo "   ✓ Files copied"

echo ""
echo "2. File inventory:"
echo "   Manuscript: manuscript.tex ($(wc -l < manuscript/manuscript.tex) lines)"
echo "   References: references.bib ($(wc -l < manuscript/references.bib) lines)"
echo "   Figures:"
ls -lh "$TEMP_DIR/figures/" | tail -n +2 | awk '{print "      " $9 " (" $5 ")"}'
echo "   Tables:"
ls -lh "$TEMP_DIR/data/tables/" | tail -n +2 | awk '{print "      " $9 " (" $5 ")"}'

echo ""
echo "3. Creating Overleaf package..."

# Create zip file (version from YAML)
OUTPUT_ZIP="manuscript_overleaf_v${VERSION}.zip"
rm -f "$OUTPUT_ZIP"

cd "$TEMP_DIR"
zip -r "../$OUTPUT_ZIP" manuscript/ figures/ data/tables/ > /dev/null
cd ..

# Cleanup
rm -rf "$TEMP_DIR"

echo "   ✓ Created: $OUTPUT_ZIP ($(du -h "$OUTPUT_ZIP" | cut -f1))"

echo ""
echo "=========================================="
echo "✅ Overleaf package ready!"
echo "=========================================="
echo ""
echo "Package for v${VERSION}: ${VERSION_DESC}"
echo ""
echo "Key changes in this version:"
"$PYTHON" -c "
import yaml
data = yaml.safe_load(open('config/numerical_claims.yaml'))
changes = data['version_history'][0]['changes']
for change in changes:
    print(f'  • {change}')
"
echo ""
echo "Next steps:"
echo "1. Go to https://www.overleaf.com"
echo "2. Click 'New Project' → 'Upload Project'"
echo "3. Upload: $OUTPUT_ZIP"
echo "4. Set compiler to 'pdfLaTeX'"
echo "5. Set main document to 'manuscript/manuscript.tex'"
echo "6. Click 'Recompile'"
echo ""
