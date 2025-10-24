#!/bin/bash
# Prepare manuscript for Overleaf upload
# Creates zip file with correct structure and path fixes

set -e

echo "=========================================="
echo "Distance Ladder Manuscript - Overleaf Prep"
echo "=========================================="
echo ""

# Check we're in correct directory
if [ ! -f "manuscript/manuscript.tex" ]; then
    echo "❌ Error: Run this script from distance_ladder/ directory"
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

# Copy figures
mkdir -p "$TEMP_DIR/figures"
cp figures/figure1_tension_evolution.png "$TEMP_DIR/figures/"
cp figures/figure2_error_budget.png "$TEMP_DIR/figures/"
cp figures/figure3_cchp_crossval_real.png "$TEMP_DIR/figures/"
cp figures/figure4_h0_compilation.png "$TEMP_DIR/figures/"
cp figures/figure5_h6_fit.png "$TEMP_DIR/figures/"

# Copy tables
mkdir -p "$TEMP_DIR/data/tables"
cp data/tables/table1_systematic_budget.tex "$TEMP_DIR/data/tables/"
cp data/tables/table2_tension_evolution.tex "$TEMP_DIR/data/tables/"
cp data/tables/table3_h0_compilation.tex "$TEMP_DIR/data/tables/"
cp data/tables/table4_cchp_crossval.tex "$TEMP_DIR/data/tables/"

echo "   ✓ Files copied"

echo ""
echo "2. Checking for higher-quality figure alternatives..."

# Check if better versions exist
if [ -f "figures/figure2_error_budget_comparison.png" ]; then
    SIZE_PLACEHOLDER=$(stat -f%z "figures/figure2_error_budget.png")
    SIZE_REAL=$(stat -f%z "figures/figure2_error_budget_comparison.png")
    if [ "$SIZE_REAL" -gt "$SIZE_PLACEHOLDER" ]; then
        echo "   ℹ️  Found better Figure 2: figure2_error_budget_comparison.png ($(($SIZE_REAL/1024)) KB vs $(($SIZE_PLACEHOLDER/1024)) KB)"
        echo "      Use this version? It will be copied as figure2_error_budget.png"
        # Auto-use the better version
        cp figures/figure2_error_budget_comparison.png "$TEMP_DIR/figures/figure2_error_budget.png"
        echo "   ✓ Using higher-quality Figure 2"
    fi
fi

echo ""
echo "3. File inventory:"
echo "   Manuscript: manuscript.tex ($(wc -l < manuscript/manuscript.tex) lines)"
echo "   References: references.bib ($(wc -l < manuscript/references.bib) lines)"
echo "   Figures:"
ls -lh "$TEMP_DIR/figures/" | tail -n +2 | awk '{print "      " $9 " (" $5 ")"}'
echo "   Tables:"
ls -lh "$TEMP_DIR/data/tables/" | tail -n +2 | awk '{print "      " $9 " (" $5 ")"}'

echo ""
echo "4. Creating Overleaf package..."

# Create zip file
OUTPUT_ZIP="manuscript_overleaf.zip"
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
echo "Next steps:"
echo ""
echo "1. Go to https://www.overleaf.com"
echo "2. Click 'New Project' → 'Upload Project'"
echo "3. Upload: $OUTPUT_ZIP"
echo "4. In Overleaf editor:"
echo "   - Set compiler to 'pdfLaTeX'"
echo "   - Set main document to 'manuscript/manuscript.tex'"
echo "5. Click 'Recompile'"
echo ""
echo "Expected compilation sequence:"
echo "   pdflatex → bibtex → pdflatex → pdflatex"
echo ""
echo "⚠️  Known placeholders in manuscript:"
echo "   - Line 26-30: [Your Name], [Your Institution], [Your Email]"
echo "   - Line ~454: [Institution] in Acknowledgments"
echo "   - Line ~461: [GitHub repository URL]"
echo ""
echo "You can compile with these placeholders for testing,"
echo "or edit them in Overleaf before compiling."
echo ""
echo "📖 Full guide: docs/LATEX_COMPILATION_GUIDE.md"
echo ""
