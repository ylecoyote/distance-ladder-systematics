# Repository Cleanup Plan

**Date**: November 4, 2025
**Purpose**: Clean GitHub repository for final manuscript submission

---

## Current Status

**Repository size**: ~20 MB (excluding .gitignored files)
**Total files tracked**: ~150
**Issues to address**: Redundant documentation, generated files, empty directories

---

## Files to Archive/Delete

### 1. Redundant Status Documentation (Root Directory)

**Issue**: Multiple overlapping status/fix documentation files created during submission prep

**Action**: CONSOLIDATE into single comprehensive document

**Files to archive** (move to `_tmp/ARCHIVE/submission_prep_logs/`):

```
✅ CRITICAL_FIX_MISSING_FIGURES.md     # Covered in FINAL_SUBMISSION_STATUS.md
✅ CITATION_FIXES.md                   # Covered in FINAL_SUBMISSION_STATUS.md
✅ LATEX_FORMATTING_FIXES.md           # Covered in FINAL_SUBMISSION_STATUS.md
✅ OVERLEAF_SUBMISSION_STATUS.md       # Covered in FINAL_SUBMISSION_STATUS.md
✅ PREPRINT_STYLE_CHANGE.md            # Covered in FINAL_SUBMISSION_STATUS.md
✅ PRE_SUBMISSION_FIXES_COMPLETE.md    # Obsolete, replaced by FINAL_SUBMISSION_STATUS.md
✅ APPENDIX_FIGURES_FIX.md             # Covered in FINAL_SUBMISSION_STATUS.md
```

**Keep**:
```
✅ FINAL_SUBMISSION_STATUS.md          # Comprehensive, up-to-date status
✅ README.md                           # Repository documentation
```

**Already tracked but obsolete**:
```
⚠️  CLEANUP_REPORT.md                 # Old cleanup report, superseded
⚠️  V8_0_RELEASE_SUMMARY.md           # Pre-submission summary, superseded
```

### 2. Generated Package Files

**Issue**: Generated ZIP file should not be tracked

**Action**: ADD to .gitignore

```
✅ manuscript_overleaf.zip (3.5 MB)    # Generated file, regenerate as needed
```

### 3. Empty Directories

**Issue**: Empty `notebooks/` directory serves no purpose

**Action**: DELETE empty directory

```
✅ notebooks/                          # Empty, no content
```

### 4. Documentation Directory Cleanup

**Files in docs/**:

**Keep**:
```
✅ docs/MANUSCRIPT_STATUS.md           # Current manuscript status
✅ docs/OVERLEAF_PACKAGE_STATUS.md     # Package documentation
✅ docs/LATEX_COMPILATION_GUIDE.md     # User guide for compilation
✅ docs/SCIENTIFIC_VALIDATION_PROTOCOL.md  # Validation procedures
```

**Already obsolete** (move to archive):
```
⚠️  docs/HIERARCHICAL_COMPONENTS.md   # Development doc, no longer relevant
```

### 5. Figures Directory Cleanup

**Currently tracked** (8 files, ~2.5 MB):
```
✅ figure1_tension_evolution.png (217 KB)           # KEEP - Main text
✅ figure2_error_budget.png (303 KB)                # KEEP - Main text
✅ figure2_error_budget_comparison.png (303 KB)     # KEEP - Alternative version
✅ figure2_error_budget_stacked.png (130 KB)        # KEEP - Alternative version
✅ figure3_cchp_crossval_real.png (305 KB)          # KEEP - Main text
✅ figure4_h0_compilation.png (204 KB)              # KEEP - Main text
✅ figure5_h6_fit.png (354 KB)                      # KEEP - Main text
✅ figure2_error_budget_comparison.pdf (56 KB)      # DELETE - Vector source (PNG sufficient)
```

**Newly recovered** (4 files, ~2.4 MB) - should ADD to tracking:
```
➕ sensitivity_correlation.png (313 KB)             # ADD - Figure 6
➕ figure_2d_correlation_sensitivity.png (427 KB)   # ADD - Figure 7
➕ posterior_joint_delta_H0.png (221 KB)            # ADD - Figure 8
➕ corner_joint_bias_fit.png (1.5 MB)               # ADD - Figure 9
```

### 6. Data Files

**Newly recovered** (2 files) - should ADD to tracking:
```
➕ data/sensitivity_correlation.csv                 # ADD - Analysis data
➕ data/2d_correlation_sensitivity_grid.npz         # Consider: Large binary, maybe gitignore
```

**Recommendation for .npz file**: Add `*.npz` to .gitignore (binary data files), provide script to regenerate

---

## .gitignore Updates

Add the following to `.gitignore`:

```gitignore
# Generated package files
manuscript_overleaf.zip
*_overleaf.zip

# Large binary data files (provide regeneration scripts instead)
*.npz

# Compiled PDFs (can be regenerated from LaTeX)
manuscript/*.pdf
Forensic_Analysis*.pdf
```

---

## Recommended Git Operations

### Step 1: Archive Redundant Documentation

```bash
# Create archive directory
mkdir -p _tmp/ARCHIVE/submission_prep_logs

# Move redundant docs
mv CRITICAL_FIX_MISSING_FIGURES.md _tmp/ARCHIVE/submission_prep_logs/
mv CITATION_FIXES.md _tmp/ARCHIVE/submission_prep_logs/
mv LATEX_FORMATTING_FIXES.md _tmp/ARCHIVE/submission_prep_logs/
mv OVERLEAF_SUBMISSION_STATUS.md _tmp/ARCHIVE/submission_prep_logs/
mv PREPRINT_STYLE_CHANGE.md _tmp/ARCHIVE/submission_prep_logs/
mv PRE_SUBMISSION_FIXES_COMPLETE.md _tmp/ARCHIVE/submission_prep_logs/
mv APPENDIX_FIGURES_FIX.md _tmp/ARCHIVE/submission_prep_logs/

# Move obsolete tracked docs
git mv CLEANUP_REPORT.md _tmp/ARCHIVE/submission_prep_logs/
git mv V8_0_RELEASE_SUMMARY.md _tmp/ARCHIVE/submission_prep_logs/
git mv docs/HIERARCHICAL_COMPONENTS.md _tmp/ARCHIVE/submission_prep_logs/
```

### Step 2: Remove Empty Directories

```bash
# Remove empty notebooks directory
rmdir notebooks
```

### Step 3: Update .gitignore

```bash
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
```

### Step 4: Add New Essential Files

```bash
# Add recovered figures to tracking
git add figures/sensitivity_correlation.png
git add figures/figure_2d_correlation_sensitivity.png
git add figures/posterior_joint_delta_H0.png
git add figures/corner_joint_bias_fit.png

# Add analysis data (CSV only, .npz now ignored)
git add data/sensitivity_correlation.csv

# Add final status document
git add FINAL_SUBMISSION_STATUS.md
```

### Step 5: Remove Unnecessary PDF

```bash
# Remove PDF version of figure (PNG sufficient)
git rm figures/figure2_error_budget_comparison.pdf
```

### Step 6: Commit Cleanup

```bash
git add .gitignore
git commit -m "Clean repository for submission

- Consolidated redundant status docs into FINAL_SUBMISSION_STATUS.md
- Archived obsolete documentation to _tmp/ARCHIVE/submission_prep_logs/
- Removed empty notebooks/ directory
- Added recovered appendix figures (4 new)
- Updated .gitignore for generated files and large binaries
- Removed redundant PDF figure

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Repository Structure After Cleanup

```
distance-ladder-systematics/
├── README.md                           # Main documentation
├── FINAL_SUBMISSION_STATUS.md          # Comprehensive submission status
├── prepare_overleaf.sh                 # Package generation script
│
├── manuscript/                         # LaTeX source
│   ├── manuscript.tex (812 lines)
│   └── references.bib (485 lines)
│
├── figures/                            # All 9 figures (PNG only)
│   ├── figure1_tension_evolution.png
│   ├── figure2_error_budget.png
│   ├── figure2_error_budget_comparison.png
│   ├── figure2_error_budget_stacked.png
│   ├── figure3_cchp_crossval_real.png
│   ├── figure4_h0_compilation.png
│   ├── figure5_h6_fit.png
│   ├── sensitivity_correlation.png
│   ├── figure_2d_correlation_sensitivity.png
│   ├── posterior_joint_delta_H0.png
│   └── corner_joint_bias_fit.png
│
├── data/                               # Data files and tables
│   ├── tables/ (8 .tex files)
│   └── sensitivity_correlation.csv
│
├── analysis/                           # Analysis scripts (13 .py files)
│   ├── create_figure*.py
│   ├── calculate_*.py
│   ├── hierarchical_*.py
│   └── ...
│
├── docs/                               # Documentation
│   ├── MANUSCRIPT_STATUS.md
│   ├── OVERLEAF_PACKAGE_STATUS.md
│   ├── LATEX_COMPILATION_GUIDE.md
│   └── SCIENTIFIC_VALIDATION_PROTOCOL.md
│
└── _tmp/                               # Ignored by git
    └── ARCHIVE/
        ├── submission_prep_logs/       # All status docs
        ├── development_figures/        # Development figures
        ├── development_scripts/        # Development scripts
        ├── development_data/           # Development data
        └── *.pdf (15 archived PDFs)
```

---

## Size Impact

### Before Cleanup
- **Tracked files**: ~150 files
- **Repository size**: ~20 MB
- **Root markdown files**: 11 files (many redundant)
- **Figures**: 8 PNG + 1 PDF

### After Cleanup
- **Tracked files**: ~145 files (-5 redundant docs)
- **Repository size**: ~23 MB (+3 MB for 4 new figures)
- **Root markdown files**: 2 files (README + FINAL_SUBMISSION_STATUS)
- **Figures**: 11 PNG (all manuscript figures)

**Net result**: Cleaner structure, all essential files tracked, redundant documentation archived

---

## Benefits of Cleanup

### 1. Clarity
- ✅ Single source of truth: FINAL_SUBMISSION_STATUS.md
- ✅ No redundant/conflicting documentation
- ✅ Clear repository structure

### 2. Maintainability
- ✅ Easy to find current status
- ✅ Historical docs archived but accessible
- ✅ Generated files not tracked

### 3. Professional Presentation
- ✅ Clean root directory (2 markdown files only)
- ✅ Logical organization
- ✅ No clutter from development process

### 4. Reproducibility
- ✅ All source figures tracked
- ✅ All analysis scripts present
- ✅ Data files available (CSV format)
- ✅ Package generation scripted

---

## Files Summary

### To Archive (Move to _tmp/ARCHIVE/submission_prep_logs/)
- CRITICAL_FIX_MISSING_FIGURES.md
- CITATION_FIXES.md
- LATEX_FORMATTING_FIXES.md
- OVERLEAF_SUBMISSION_STATUS.md
- PREPRINT_STYLE_CHANGE.md
- PRE_SUBMISSION_FIXES_COMPLETE.md
- APPENDIX_FIGURES_FIX.md
- CLEANUP_REPORT.md (git mv)
- V8_0_RELEASE_SUMMARY.md (git mv)
- docs/HIERARCHICAL_COMPONENTS.md (git mv)

### To Delete
- notebooks/ (empty directory)
- figures/figure2_error_budget_comparison.pdf (git rm)

### To Add to .gitignore
- manuscript_overleaf.zip
- *_overleaf.zip
- *.npz
- manuscript/*.pdf
- Forensic_Analysis*.pdf

### To Add to Tracking
- figures/sensitivity_correlation.png
- figures/figure_2d_correlation_sensitivity.png
- figures/posterior_joint_delta_H0.png
- figures/corner_joint_bias_fit.png
- data/sensitivity_correlation.csv
- FINAL_SUBMISSION_STATUS.md

---

## Verification Checklist

After cleanup, verify:

```bash
# Check no generated files tracked
git ls-files | grep -E "\.(zip|npz)$"
# Should output: NOTHING

# Check all markdown in root
ls -1 *.md
# Should output: README.md, FINAL_SUBMISSION_STATUS.md

# Check all figures present
ls -1 figures/*.png | wc -l
# Should output: 11

# Check .gitignore covers generated files
git status --short
# Should not show manuscript_overleaf.zip or .npz files

# Verify repository size reasonable
du -sh .git/
# Should be ~25-30 MB (includes history)
```

---

## Execution Plan

**Option 1: Execute all at once** (recommended for experienced Git users)
```bash
./scripts/cleanup_repo.sh  # If we create this script
```

**Option 2: Execute step-by-step** (recommended for review at each stage)
1. Create archive directory
2. Move files to archive
3. Update .gitignore
4. Add new files
5. Remove obsolete files
6. Commit changes
7. Verify cleanup

---

## Final Notes

**This cleanup**:
- ✅ Preserves all important information (archived, not deleted)
- ✅ Maintains full Git history
- ✅ Improves repository professionalism
- ✅ Makes current status immediately clear
- ✅ Removes development artifacts

**After cleanup**:
- Anyone cloning the repo sees clean structure
- FINAL_SUBMISSION_STATUS.md provides complete context
- All manuscript files ready for submission
- Development history preserved in archive

---

**Date**: November 4, 2025
**Status**: Ready to execute
**Estimated time**: 10-15 minutes
