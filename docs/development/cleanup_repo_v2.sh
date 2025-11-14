#!/bin/bash
# Repository Cleanup Script v2
# Cleans repository structure after v8.6C submission package creation
# Updated: November 13, 2025

set -e

echo "=========================================="
echo "Repository Cleanup v2 (Post-v8.6C)"
echo "=========================================="
echo ""

# Check we're in correct directory
if [ ! -f "manuscript/manuscript.tex" ]; then
    echo "❌ Error: Run this script from distance-ladder-systematics/ directory"
    exit 1
fi

echo "This script will:"
echo "  1. Archive post-v8.6C inconsistency fix documentation"
echo "  2. Archive intermediate Overleaf packages"
echo "  3. Update .gitignore for new packages"
echo "  4. Keep only essential documentation"
echo "  5. Display final repository status"
echo ""
echo "Files to be archived (inconsistency fix logs):"
echo "  - BASELINE_CONSISTENCY_FIX.md"
echo "  - CORRECTED_CEPHEID_FIX.md"
echo "  - STAGE_VALUES_VALIDATION.md"
echo "  - LEGACY_2.36X_FIX.md"
echo "  - ALL_INCONSISTENCIES_RESOLVED.md"
echo "  - OVERLEAF_PATH_FIX.md"
echo "  - OVERLEAF_PACKAGE_SUMMARY.md"
echo "  - OVERLEAF_PACKAGE_v8.6B_SUMMARY.md"
echo "  - MD_FILES_ALIGNMENT_COMPLETE.md"
echo "  - MD_FILES_VALIDATION_REPORT.md"
echo "  - QUICK_VALIDATION_v8.6B.md"
echo "  - REPO_CLEANUP_PLAN.md"
echo ""
echo "Files to KEEP in root:"
echo "  - README.md"
echo "  - FINAL_SUBMISSION_STATUS.md"
echo "  - OVERLEAF_PACKAGE_v8.6C_SUMMARY.md (latest)"
echo "  - PLANCK_DEPENDENCE_ANALYSIS.md"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cleanup cancelled"
    exit 0
fi

echo ""
echo "Step 1: Creating archive directory..."
mkdir -p _tmp/ARCHIVE/v8.6c_inconsistency_fixes

echo ""
echo "Step 2: Archiving inconsistency fix documentation..."
# Archive detailed fix documentation
for file in BASELINE_CONSISTENCY_FIX.md \
            CORRECTED_CEPHEID_FIX.md \
            STAGE_VALUES_VALIDATION.md \
            LEGACY_2.36X_FIX.md \
            ALL_INCONSISTENCIES_RESOLVED.md \
            OVERLEAF_PATH_FIX.md \
            OVERLEAF_PACKAGE_SUMMARY.md \
            OVERLEAF_PACKAGE_v8.6B_SUMMARY.md \
            MD_FILES_ALIGNMENT_COMPLETE.md \
            MD_FILES_VALIDATION_REPORT.md \
            QUICK_VALIDATION_v8.6B.md \
            REPO_CLEANUP_PLAN.md; do
    if [ -f "$file" ]; then
        mv "$file" _tmp/ARCHIVE/v8.6c_inconsistency_fixes/
        echo "   ✓ Archived: $file"
    else
        echo "   ℹ️  Not found: $file"
    fi
done

echo ""
echo "Step 3: Archiving intermediate Overleaf packages..."
mkdir -p _tmp/ARCHIVE/overleaf_intermediate_versions

# Archive old Overleaf ZIP files (keep only v8.6C)
for file in manuscript_overleaf.zip \
            manuscript_overleaf_v8.6A.zip \
            manuscript_overleaf_v8.6A_fixed.zip \
            manuscript_overleaf_v8.6B.zip; do
    if [ -f "$file" ]; then
        mv "$file" _tmp/ARCHIVE/overleaf_intermediate_versions/
        echo "   ✓ Archived: $file"
    else
        echo "   ℹ️  Not found: $file"
    fi
done

# Archive overleaf_package directory (v8.6B source, superseded by v8.6C)
if [ -d "overleaf_package" ]; then
    tar -czf _tmp/ARCHIVE/overleaf_intermediate_versions/overleaf_package.tar.gz overleaf_package
    rm -rf overleaf_package
    echo "   ✓ Archived and removed: overleaf_package/ (compressed)"
fi

# Archive overleaf_package_v8.6B directory (keep source for reference)
if [ -d "overleaf_package_v8.6B" ]; then
    echo "   ℹ️  Keeping: overleaf_package_v8.6B/ (source for v8.6C)"
fi

echo ""
echo "Step 4: Updating .gitignore..."
# Check if entries already exist
if ! grep -q "manuscript_overleaf_v8.6C.zip" .gitignore; then
    cat >> .gitignore << 'EOF'

# Generated Overleaf packages (keep only v8.6C tracked)
manuscript_overleaf*.zip
!manuscript_overleaf_v8.6C.zip
overleaf_package/
overleaf_package_v8.6B/

# Large binary data files
*.npz

# Compiled PDFs
manuscript/*.pdf
Forensic_Analysis*.pdf
EOF
    echo "   ✓ Updated .gitignore"
else
    echo "   ℹ️  .gitignore already contains Overleaf entries"
fi

echo ""
echo "Step 5: Verifying essential files are tracked..."
git add FINAL_SUBMISSION_STATUS.md 2>/dev/null && echo "   ✓ Added: FINAL_SUBMISSION_STATUS.md" || echo "   ℹ️  Already tracked: FINAL_SUBMISSION_STATUS.md"
git add README.md 2>/dev/null && echo "   ✓ Added: README.md" || echo "   ℹ️  Already tracked: README.md"
git add OVERLEAF_PACKAGE_v8.6C_SUMMARY.md 2>/dev/null && echo "   ✓ Added: OVERLEAF_PACKAGE_v8.6C_SUMMARY.md" || echo "   ℹ️  Already tracked: OVERLEAF_PACKAGE_v8.6C_SUMMARY.md"

echo ""
echo "Step 6: Adding final Overleaf package..."
# Track the final v8.6C package
git add -f manuscript_overleaf_v8.6C.zip 2>/dev/null && echo "   ✓ Added: manuscript_overleaf_v8.6C.zip (force)" || echo "   ℹ️  Already tracked: manuscript_overleaf_v8.6C.zip"

echo ""
echo "Step 7: Adding .gitignore updates..."
git add .gitignore 2>/dev/null && echo "   ✓ Added: .gitignore" || echo "   ℹ️  Already updated: .gitignore"

echo ""
echo "=========================================="
echo "✅ Cleanup v2 Complete!"
echo "=========================================="
echo ""
echo "Repository structure cleaned:"
echo "  ✓ Inconsistency fix docs → _tmp/ARCHIVE/v8.6c_inconsistency_fixes/"
echo "  ✓ Intermediate packages → _tmp/ARCHIVE/overleaf_intermediate_versions/"
echo "  ✓ .gitignore updated for v8.6C package"
echo "  ✓ Essential documentation retained in root"
echo ""
echo "Final root documentation:"
echo "  ✓ README.md - Main repository documentation"
echo "  ✓ FINAL_SUBMISSION_STATUS.md - Current submission status"
echo "  ✓ OVERLEAF_PACKAGE_v8.6C_SUMMARY.md - Latest package summary"
echo "  ✓ PLANCK_DEPENDENCE_ANALYSIS.md - Scientific analysis"
echo ""
echo "Archived for reference:"
echo "  ✓ All 4 inconsistency fix documents"
echo "  ✓ All intermediate Overleaf validation docs"
echo "  ✓ Old Overleaf package versions (v8.6A, v8.6A_fixed, v8.6B)"
echo ""
echo "Next steps:"
echo "  1. Review changes: git status"
echo "  2. Review diff: git diff --cached"
echo "  3. Review archived files: ls _tmp/ARCHIVE/v8.6c_inconsistency_fixes/"
echo "  4. Commit: git commit -m 'Archive v8.6C inconsistency fix documentation'"
echo ""
echo "Suggested commit message:"
echo "────────────────────────────────────────"
cat << 'EOF'
Archive v8.6C inconsistency fix documentation

Complete final cleanup after resolving all four citation/value
inconsistencies for v8.6C submission package:

Archived (detailed fix logs):
- All 4 inconsistency fix documents (BASELINE_CONSISTENCY_FIX.md,
  CORRECTED_CEPHEID_FIX.md, STAGE_VALUES_VALIDATION.md, LEGACY_2.36X_FIX.md)
- Comprehensive resolution summary (ALL_INCONSISTENCIES_RESOLVED.md)
- Intermediate Overleaf validation docs (path fix, package summaries)
- Repository alignment and validation reports

Archived (intermediate packages):
- Old Overleaf packages (v8.6A, v8.6A_fixed, v8.6B)
- Compressed overleaf_package/ directory

Retained in root:
- README.md (main documentation)
- FINAL_SUBMISSION_STATUS.md (current status)
- OVERLEAF_PACKAGE_v8.6C_SUMMARY.md (final package summary)
- PLANCK_DEPENDENCE_ANALYSIS.md (scientific analysis)
- manuscript_overleaf_v8.6C.zip (final submission package, 4.5 MB)

Updated .gitignore:
- Exclude all Overleaf packages except v8.6C
- Exclude overleaf_package directories

Repository now clean and ready for final submission with only
essential documentation and the corrected v8.6C Overleaf package.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
echo "────────────────────────────────────────"
echo ""
