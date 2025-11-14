# .md Files Validation Report - v8.6A Referee Response Complete

**Date:** November 12, 2025
**Status:** ⚠️ UPDATES REQUIRED
**Manuscript Version:** v8.6A (All referee feedback incorporated)

---

## Critical Value Updates Required

### From v8.5/v8.5A → v8.6A (Referee Response)

| Item | Old Value | New Value | Reason |
|------|-----------|-----------|--------|
| **Systematic sources** | 10-11 sources | **9 sources** | Removed covariant crowding standalone term |
| **Correlation matrix** | 10×10 | **9×9** | Matches 9 sources |
| **σ_sys,corr** | 3.14 km/s/Mpc | **1.71 km/s/Mpc** | Conservative peer review methodology |
| **Underestimate factor** | 2.9× | **1.6×** | Updated with 9-source budget |
| **Tension (Planck-rel)** | 0.9σ | **1.2σ** | More conservative, defensible |
| **Bias corrections** | "-1-1-1" or "-3.0" | **"0 -2.5 -1.0 = -3.5"** | Explicit baseline (Scenario A + Prior 1) |
| **Period correction** | -1.0 km/s/Mpc | **-2.5 km/s/Mpc** | Mid-range of explicit bracket [-1.5, -3.5] |
| **Metallicity (Prior 1)** | Varies | **-1.0 km/s/Mpc** | γ = -0.2 ± 0.1 baseline |
| **Parallax (Scenario A)** | -1.0 km/s/Mpc | **0 km/s/Mpc** | Adopt SH0ES internally-fitted ZP |
| **Table count** | 6 tables | **8 tables** | Added correlation matrix + anchor weights |
| **Figure count** | 6-9 figures | **16 figures** | PDFs + PNGs + supplementary |

---

## Files Requiring Updates

### 🔴 CRITICAL UPDATES NEEDED

1. **README.md** (Lines 76, 191, multiple)
   - Line 76: "11 systematic error sources" → **9 sources**
   - Line 191: "11 systematic error sources" → **9 sources**
   - Line 18: σ_sys = 1.71 ✓ (correct)
   - Line 20: Tension 1.2σ ✓ (correct)
   - Branch reference line 8 needs update

2. **FINAL_SUBMISSION_STATUS.md** (Lines 196, 202, 269-272, multiple)
   - Line 196: "10 systematic error sources" → **9 sources**
   - Line 202: "10×10 systematic correlations" → **9×9**
   - Lines 269-272: Outdated "Three Bias Corrections"
     - Old: -1.0 parallax, -1.0 period, metallicity part of budget
     - New: **0 parallax (Scenario A), -2.5 period, -1.0 metallicity**
   - Multiple references to 2.9× → **1.6×**
   - Multiple references to 0.9σ → **1.2σ**
   - Multiple references to 3.14 km/s/Mpc → **1.71 km/s/Mpc**

3. **docs/MANUSCRIPT_STATUS.md**
   - Check for 10 sources → 9 sources
   - Check for old tension/factor values

4. **docs/OVERLEAF_PACKAGE_STATUS.md**
   - Update table count
   - Update figure count
   - Update key values

---

## Files Already Up-to-Date ✅

1. **OVERLEAF_PACKAGE_SUMMARY.md** (Just created)
   - ✅ All v8.6A values correct
   - ✅ 9 sources documented
   - ✅ 9×9 matrix documented
   - ✅ Referee feedback comprehensive
   - ✅ All baseline values correct

2. **manuscript/manuscript.tex** (Main manuscript)
   - ✅ All referee corrections applied
   - ✅ 9×9 matrix throughout
   - ✅ Correction scheme harmonized

3. **data/tables/*.tex** (All table files)
   - ✅ table1_systematic_budget.tex: 9 sources, CCHP row removed
   - ✅ table2_tension_evolution.tex: Stage 4 = 1.65, Stage 5 = 1.89
   - ✅ table3_h0_compilation.tex: σ_sys,corr = 1.71
   - ✅ table_correlation_matrix.tex: 9×9 matrix

---

## Specific Updates Required

### README.md

**Line 76:**
```markdown
# BEFORE:
│   ├── systematic_error_budget.csv        # 11 systematic error sources

# AFTER:
│   ├── systematic_error_budget.csv        # 9 systematic error sources
```

**Line 191:**
```markdown
# BEFORE:
- **systematic_error_budget.csv**: 11 systematic error sources with SH0ES vs our assessments

# AFTER:
- **systematic_error_budget.csv**: 9 systematic error sources with SH0ES vs our assessments (after removing covariant crowding standalone term per peer review)
```

**Line 8:**
```markdown
# BEFORE:
**Branch**: revision-v8-5a-planck-independence (to be merged with revision-m1-peer-review)

# AFTER:
**Branch**: revision-m1-peer-review (v8.6A referee response complete)
```

### FINAL_SUBMISSION_STATUS.md

**Lines 196, 202:**
```markdown
# BEFORE (Line 196):
1. `table1_systematic_budget.tex` - 10 systematic error sources

# AFTER:
1. `table1_systematic_budget.tex` - 9 systematic error sources (after removing covariant crowding standalone term)

# BEFORE (Line 202):
7. `table_correlation_matrix.tex` - 10×10 systematic correlations

# AFTER:
7. `table_correlation_matrix.tex` - 9×9 systematic correlations
```

**Lines 269-273 (Three Bias Corrections section):**
```markdown
# BEFORE:
### Three Bias Corrections
1. **Parallax zero point**: -1.0 km/s/Mpc
2. **Period distribution**: -1.0 km/s/Mpc
3. **Metallicity**: Part of systematic budget

**Total correction**: -3.0 km/s/Mpc (73.17 → 70.17)

# AFTER:
### Three Bias Corrections (Scenario A + Prior 1 Baseline)
1. **Parallax zero point (Scenario A)**: 0 km/s/Mpc (adopt SH0ES internally-fitted ZP)
2. **Period distribution**: -2.5 km/s/Mpc (mid-range of explicit bracket [-1.5, -3.5])
3. **Metallicity (Prior 1)**: -1.0 km/s/Mpc (γ = -0.2 ± 0.1, 2025 consensus)

**Total correction**: -3.5 km/s/Mpc (73.17 → 69.67)
```

**Update all 2.9× references:**
```markdown
# Find and replace:
2.9× → 1.6×
3.14 km/s/Mpc → 1.71 km/s/Mpc
0.9σ → 1.2σ
```

---

## Validation Checklist

### README.md
- [ ] Update "11 systematic" → "9 systematic" (2 instances)
- [ ] Update branch reference to revision-m1-peer-review
- [ ] Verify all key values (σ_sys, tension, factors)
- [ ] Update table count if needed
- [ ] Check figure count references

### FINAL_SUBMISSION_STATUS.md
- [ ] Update "10 systematic" → "9 systematic"
- [ ] Update "10×10" → "9×9"
- [ ] Update Three Bias Corrections section completely
- [ ] Replace all 2.9× → 1.6×
- [ ] Replace all 0.9σ → 1.2σ
- [ ] Replace all 3.14 → 1.71 km/s/Mpc
- [ ] Add v8.6A final referee response completion note

### PLANCK_DEPENDENCE_ANALYSIS.md
- [ ] Verify all values match v8.6A
- [ ] Check if any 10-source references exist

### docs/ Files
- [ ] docs/MANUSCRIPT_STATUS.md: Check for outdated values
- [ ] docs/OVERLEAF_PACKAGE_STATUS.md: Update counts and values
- [ ] docs/SCIENTIFIC_VALIDATION_PROTOCOL.md: Verify protocols current

---

## Priority Order

**HIGH PRIORITY** (User-facing, critical for submission):
1. README.md (main project documentation)
2. FINAL_SUBMISSION_STATUS.md (submission status)
3. OVERLEAF_PACKAGE_SUMMARY.md (already done ✓)

**MEDIUM PRIORITY** (Supporting documentation):
4. docs/MANUSCRIPT_STATUS.md
5. docs/OVERLEAF_PACKAGE_STATUS.md
6. PLANCK_DEPENDENCE_ANALYSIS.md

**LOW PRIORITY** (Historical/internal):
7. Other .md files in docs/
8. .claude/ directory files (internal configuration)

---

## Action Plan

1. **Update README.md** (3 changes)
   - Systematic sources: 11 → 9
   - Branch reference update
   - Verify all key values

2. **Update FINAL_SUBMISSION_STATUS.md** (major revision)
   - Systematic sources: 10 → 9
   - Matrix: 10×10 → 9×9
   - Bias corrections section (complete rewrite)
   - Global find/replace: 2.9×, 0.9σ, 3.14 km/s/Mpc
   - Add v8.6A completion note

3. **Check and update docs/ files as needed**
   - Quick scan for outdated values
   - Update if found

4. **Create completion report**
   - Document all changes made
   - Verify alignment with manuscript v8.6A
   - Confirm all referee feedback reflected

---

## Notes

- OVERLEAF_PACKAGE_SUMMARY.md was just created with all correct v8.6A values ✓
- Manuscript and all tables are already correct ✓
- Focus updates on root-level .md files and docs/ directory
- .claude/ directory files are internal and less critical for now

---

**Status:** Ready to proceed with systematic updates
**Estimated Time:** 30-45 minutes
**Priority:** HIGH (ensures documentation alignment before final submission)
