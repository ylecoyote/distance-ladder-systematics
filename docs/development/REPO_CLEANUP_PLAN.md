# Repository Cleanup Plan

**Date**: November 12, 2025 (Updated)
**Original**: November 4, 2025
**Purpose**: Clean GitHub repository for final manuscript submission

---

## Current Status (Updated November 12, 2025)

**Current branch**: `revision-v8-5a-planck-independence`
**Repository size**: ~15 MB (.git directory)
**Total files tracked**: 86 files
**Status**: Partial cleanup completed; additional files added for v8.5A peer review

### Recent Activity (Nov 10-12, 2025)
- ✅ Implemented all 8 Linear issues from v8.5A peer review feedback (AWI-171 through AWI-178)
- ✅ Added 3 new analysis scripts (robustness checks, correlation sensitivity, random-effects)
- ✅ Added 5 new data files (CSV results from robustness analyses)
- ✅ Added 1 new figure (extended_correlation_sensitivity.png)
- ✅ Updated manuscript.tex throughout (Planck-independence framing)

### Outstanding Issues
- ⚠️ Root directory still has 8 markdown files (should consolidate to 2-3)
- ⚠️ Some redundant documentation files remain

---

## Files to Archive/Delete

### 1. Root Directory Documentation Status (Updated Nov 12, 2025)

**Current root markdown files** (8 total):

```
✅ README.md                           # Repository documentation - KEEP
✅ FINAL_SUBMISSION_STATUS.md          # v8.0 submission status - KEEP
⚠️  EXECUTIVE_SUMMARY.md               # Nov 10 project summary - DECIDE: Keep or archive?
⚠️  FINAL_REVIEW_CHECKLIST.md          # Nov 5 pre-submission checklist - ARCHIVE
⚠️  PEER_REVIEW_M1_RESPONSE_LETTER.md  # Nov 5 M1 response letter - KEEP (important)
⚠️  PEER_REVIEW_M1_SYNTHESIS.md        # Nov 5 M1 synthesis - ARCHIVE (covered in response letter)
⚠️  PLANCK_DEPENDENCE_ANALYSIS.md      # Nov 12 v8.5A analysis - KEEP (recent work)
⚠️  REPO_CLEANUP_PLAN.md               # This file - KEEP (planning doc)
```

**Recommendation**:

**KEEP (Essential documentation)**:
```
✅ README.md                           # Project overview
✅ FINAL_SUBMISSION_STATUS.md          # v8.0 status
✅ PEER_REVIEW_M1_RESPONSE_LETTER.md   # Referee correspondence
✅ PLANCK_DEPENDENCE_ANALYSIS.md       # v8.5A implementation tracking
✅ REPO_CLEANUP_PLAN.md                # Repository maintenance plan
```

**ARCHIVE to `_tmp/ARCHIVE/review_process/`**:
```
⚠️  FINAL_REVIEW_CHECKLIST.md          # Pre-submission checklist (completed)
⚠️  PEER_REVIEW_M1_SYNTHESIS.md        # Covered in response letter
⚠️  EXECUTIVE_SUMMARY.md               # Project summary (optional)
```

**Result**: 5 essential files in root (still reasonable for active development project)

---

### 1b. Previously Cleaned Files (DONE)

**Files already archived** (move to `_tmp/ARCHIVE/submission_prep_logs/`):

```
✅ CRITICAL_FIX_MISSING_FIGURES.md     # Covered in FINAL_SUBMISSION_STATUS.md
✅ CITATION_FIXES.md                   # Covered in FINAL_SUBMISSION_STATUS.md
✅ LATEX_FORMATTING_FIXES.md           # Covered in FINAL_SUBMISSION_STATUS.md
✅ OVERLEAF_SUBMISSION_STATUS.md       # Covered in FINAL_SUBMISSION_STATUS.md
✅ PREPRINT_STYLE_CHANGE.md            # Covered in FINAL_SUBMISSION_STATUS.md
✅ PRE_SUBMISSION_FIXES_COMPLETE.md    # Obsolete, replaced by FINAL_SUBMISSION_STATUS.md
✅ APPENDIX_FIGURES_FIX.md             # Covered in FINAL_SUBMISSION_STATUS.md
✅ CLEANUP_REPORT.md                   # Old cleanup report, superseded
✅ V8_0_RELEASE_SUMMARY.md             # Pre-submission summary, superseded
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

### 5. Figures Directory Status (Updated Nov 12, 2025)

**Currently tracked** (13 PNG files):
```
✅ figure1_tension_evolution.png                    # Main text Figure 1
✅ figure2_error_budget.png                         # Main text Figure 2
✅ figure2_error_budget_comparison.png              # Alternative version
✅ figure2_error_budget_stacked.png                 # Alternative version
✅ figure3_cchp_crossval_real.png                   # Main text Figure 3
✅ figure4_h0_compilation.png                       # Main text Figure 4
✅ figure5_h6_fit.png                               # Main text Figure 5
✅ sensitivity_correlation.png                      # Appendix Figure 6
✅ figure_2d_correlation_sensitivity.png            # Appendix Figure 7
✅ posterior_joint_delta_H0.png                     # Appendix Figure 8
✅ corner_joint_bias_fit.png                        # Appendix Figure 9
✅ period_distribution_sensitivity.png              # Supplementary analysis
✅ extended_correlation_sensitivity.png             # NEW - v8.5A robustness (AWI-175)
```

**Status**: All manuscript figures now tracked ✅

### 6. Data Files Status (Updated Nov 12, 2025)

**v8.5A Peer Review Implementation Added** (Nov 10-12, 2025):
```
✅ correlation_matrix_literature_justification.csv  # AWI-175: Literature citations for ρ values
✅ cosmic_chronometer_random_effects_results.csv    # AWI-176: Random-effects H(z) fit results
✅ extended_correlation_sensitivity_results.csv     # AWI-175: ρ ∈ [0.0, 0.8] sweep
✅ jwst_robustness_results.csv                      # AWI-174: Jackknife + robust estimators
✅ jwst_scatter_ratio_robustness.csv                # AWI-174: Scatter ratio analysis
```

**Previously tracked**:
```
✅ sensitivity_correlation.csv                      # Original correlation sensitivity
✅ correlation_matrix.csv                           # Baseline correlation matrix
✅ correlation_matrix_updated.csv                   # Updated correlations (post-covariant removal)
```

**Binary files** (.npz): Should remain gitignored, regenerated by scripts

### 7. Analysis Scripts Status (Updated Nov 12, 2025)

**v8.5A Implementation Scripts** (NEW):
```
✅ analysis/jwst_crossval_robustness.py             # AWI-174: Jackknife + MAD + Tukey biweight
✅ analysis/extended_correlation_sensitivity.py     # AWI-175: Extended ρ-sweep to 0.8
✅ analysis/cosmic_chronometer_fit_random_effects.py # AWI-176: Random-effects error scaling
```

**Existing analysis pipeline** (~13-15 Python scripts tracked)

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

### Before Cleanup (Nov 4, 2025)
- **Tracked files**: ~150 files
- **Repository size**: ~20 MB
- **Root markdown files**: 11 files (many redundant)
- **Figures**: 8 PNG + 1 PDF

### Current Status (Nov 12, 2025)
- **Tracked files**: 86 files ✅ (significantly reduced)
- **Repository size**: ~15 MB ✅ (.git directory)
- **Root markdown files**: 8 files ⚠️ (still needs consolidation)
- **Figures**: 13 PNG ✅ (all manuscript + supplementary figures tracked)

### Target After Final Cleanup
- **Tracked files**: ~85 files (minimal change)
- **Repository size**: ~15 MB (stable)
- **Root markdown files**: 2-3 files (README + FINAL_SUBMISSION_STATUS + optional v8.5A tracking)
- **Figures**: 13 PNG (no change, all needed)

**Net result so far**: Substantial cleanup achieved (150 → 86 files), v8.5A updates integrated, but root directory documentation still needs final consolidation

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

## Update History

### November 12, 2025
- **Status**: Partially complete, v8.5A updates integrated
- **Changes since Nov 4**:
  - ✅ Reduced tracked files from 150 → 86
  - ✅ Added v8.5A peer review implementation files (3 scripts, 5 data files, 1 figure)
  - ✅ Updated manuscript.tex with Planck-independence framing (AWI-171 through AWI-178)
  - ⚠️ Root markdown files: 8 remain (target: 5 essential)
  - ⚠️ Still need to archive: FINAL_REVIEW_CHECKLIST.md, PEER_REVIEW_M1_SYNTHESIS.md, EXECUTIVE_SUMMARY.md
- **Next steps**:
  - Optional: Archive 3 remaining non-essential markdown files
  - Merge `revision-v8-5a-planck-independence` → `revision-m1-peer-review`
  - Prepare for v8.6A submission

### November 4, 2025
- **Status**: Initial planning, ready to execute
- **Estimated time**: 10-15 minutes for core cleanup

---

**Last updated**: November 12, 2025
**Current status**: Substantial progress achieved, repository in good shape for active development
