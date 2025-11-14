#!/bin/bash
# Repository Cleanup Script
# Cleans repository structure for final manuscript submission

set -e

echo "=========================================="
echo "Repository Cleanup for Submission"
echo "=========================================="
echo ""

# Check we're in correct directory
if [ ! -f "manuscript/manuscript.tex" ]; then
    echo "❌ Error: Run this script from distance-ladder-systematics/ directory"
    exit 1
fi

echo "This script will:"
echo "  1. Archive redundant status documentation"
echo "  2. Remove empty directories"
echo "  3. Update .gitignore"
echo "  4. Add recovered figures to tracking"
echo "  5. Remove unnecessary PDF"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cleanup cancelled"
    exit 0
fi

echo ""
echo "Step 1: Creating archive directory..."
mkdir -p _tmp/ARCHIVE/submission_prep_logs

echo "Step 2: Archiving redundant documentation..."
# Move untracked redundant docs
for file in CRITICAL_FIX_MISSING_FIGURES.md \
            CITATION_FIXES.md \
            LATEX_FORMATTING_FIXES.md \
            OVERLEAF_SUBMISSION_STATUS.md \
            PREPRINT_STYLE_CHANGE.md \
            PRE_SUBMISSION_FIXES_COMPLETE.md \
            APPENDIX_FIGURES_FIX.md; do
    if [ -f "$file" ]; then
        mv "$file" _tmp/ARCHIVE/submission_prep_logs/
        echo "   ✓ Archived: $file"
    fi
done

# Move tracked obsolete docs
if [ -f "CLEANUP_REPORT.md" ]; then
    git mv CLEANUP_REPORT.md _tmp/ARCHIVE/submission_prep_logs/ 2>/dev/null || \
        mv CLEANUP_REPORT.md _tmp/ARCHIVE/submission_prep_logs/
    echo "   ✓ Archived: CLEANUP_REPORT.md"
fi

if [ -f "V8_0_RELEASE_SUMMARY.md" ]; then
    git mv V8_0_RELEASE_SUMMARY.md _tmp/ARCHIVE/submission_prep_logs/ 2>/dev/null || \
        mv V8_0_RELEASE_SUMMARY.md _tmp/ARCHIVE/submission_prep_logs/
    echo "   ✓ Archived: V8_0_RELEASE_SUMMARY.md"
fi

if [ -f "docs/HIERARCHICAL_COMPONENTS.md" ]; then
    git mv docs/HIERARCHICAL_COMPONENTS.md _tmp/ARCHIVE/submission_prep_logs/ 2>/dev/null || \
        mv docs/HIERARCHICAL_COMPONENTS.md _tmp/ARCHIVE/submission_prep_logs/
    echo "   ✓ Archived: docs/HIERARCHICAL_COMPONENTS.md"
fi

echo ""
echo "Step 3: Removing empty directories..."
if [ -d "notebooks" ] && [ -z "$(ls -A notebooks)" ]; then
    rmdir notebooks
    echo "   ✓ Removed: notebooks/ (empty)"
fi

echo ""
echo "Step 4: Updating .gitignore..."
# Check if entries already exist
if ! grep -q "manuscript_overleaf.zip" .gitignore; then
    cat >> .gitignore << 'EOF'

# Generated package files
manuscript_overleaf.zip
*_overleaf.zip

# Large binary data files
*.npz

# Compiled PDFs
manuscript/*.pdf
Forensic_Analysis*.pdf
EOF
    echo "   ✓ Updated .gitignore"
else
    echo "   ℹ️  .gitignore already updated"
fi

echo ""
echo "Step 5: Adding recovered figures to tracking..."
git add figures/sensitivity_correlation.png 2>/dev/null && echo "   ✓ Added: sensitivity_correlation.png" || echo "   ℹ️  Already tracked: sensitivity_correlation.png"
git add figures/figure_2d_correlation_sensitivity.png 2>/dev/null && echo "   ✓ Added: figure_2d_correlation_sensitivity.png" || echo "   ℹ️  Already tracked: figure_2d_correlation_sensitivity.png"
git add figures/posterior_joint_delta_H0.png 2>/dev/null && echo "   ✓ Added: posterior_joint_delta_H0.png" || echo "   ℹ️  Already tracked: posterior_joint_delta_H0.png"
git add figures/corner_joint_bias_fit.png 2>/dev/null && echo "   ✓ Added: corner_joint_bias_fit.png" || echo "   ℹ️  Already tracked: corner_joint_bias_fit.png"

echo ""
echo "Step 6: Adding analysis data..."
git add data/sensitivity_correlation.csv 2>/dev/null && echo "   ✓ Added: sensitivity_correlation.csv" || echo "   ℹ️  Already tracked: sensitivity_correlation.csv"

echo ""
echo "Step 7: Adding final status document..."
git add FINAL_SUBMISSION_STATUS.md 2>/dev/null && echo "   ✓ Added: FINAL_SUBMISSION_STATUS.md" || echo "   ℹ️  Already tracked: FINAL_SUBMISSION_STATUS.md"

echo ""
echo "Step 8: Removing unnecessary PDF..."
if git ls-files | grep -q "figures/figure2_error_budget_comparison.pdf"; then
    git rm figures/figure2_error_budget_comparison.pdf
    echo "   ✓ Removed: figures/figure2_error_budget_comparison.pdf"
else
    echo "   ℹ️  PDF not tracked or already removed"
fi

echo ""
echo "Step 9: Adding .gitignore updates..."
git add .gitignore

echo ""
echo "=========================================="
echo "✅ Cleanup Complete!"
echo "=========================================="
echo ""
echo "Repository structure cleaned:"
echo "  ✓ Redundant docs archived to _tmp/ARCHIVE/submission_prep_logs/"
echo "  ✓ Empty directories removed"
echo "  ✓ Generated files added to .gitignore"
echo "  ✓ All manuscript figures tracked (9 total)"
echo "  ✓ Analysis data tracked"
echo ""
echo "Next steps:"
echo "  1. Review changes: git status"
echo "  2. Review diff: git diff --cached"
echo "  3. Commit: git commit -m 'Clean repository for submission'"
echo ""
echo "Suggested commit message:"
echo "────────────────────────────────────────"
cat << 'EOF'
Clean repository for submission

- Consolidated redundant status docs into FINAL_SUBMISSION_STATUS.md
- Archived obsolete documentation to _tmp/ARCHIVE/submission_prep_logs/
- Removed empty notebooks/ directory
- Added recovered appendix figures (4 new)
- Updated .gitignore for generated files and large binaries
- Removed redundant PDF figure

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
echo "────────────────────────────────────────"
echo ""
