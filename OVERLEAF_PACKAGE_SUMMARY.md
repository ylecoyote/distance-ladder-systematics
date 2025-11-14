# Overleaf Package Summary v8.6A - Referee Response Complete

**Date:** November 12, 2025
**Version:** 8.6A (M1 Peer Review Response)
**Status:** ✅ Ready for ApJ Submission
**Package:** `manuscript_overleaf_v8.6A.zip` (4.5 MB)

---

## Package Contents

### Core Files
- ✅ `manuscript.tex` (123 KB) - Main manuscript with all referee corrections
- ✅ `references.bib` (18 KB) - Complete bibliography with 2024-2025 citations
- ✅ `aastex701.cls` (401 KB) - AASTeX document class
- ✅ `README.txt` (3.5 KB) - Complete compilation instructions

### Tables (8 files)
- ✅ `table1_systematic_budget.tex` - 9-source error budget (CCHP row removed)
- ✅ `table2_tension_evolution.tex` - 5-stage tension reduction
- ✅ `table3_h0_compilation.tex` - Multi-method H₀ convergence (σ_sys updated to 1.71)
- ✅ `table4_cchp_crossval.tex` - CCHP cross-validation
- ✅ `table5_jwst_crossvalidation.tex` - Per-galaxy JWST comparison
- ✅ `table6_cosmic_chronometers.tex` - H(z) measurements
- ✅ `table_anchor_weights.tex` - Anchor weights
- ✅ `table_correlation_matrix.tex` - 9×9 correlation matrix

### Figures (16 files)
- ✅ `figure1_tension_evolution.pdf` - Stage-wise tension reduction
- ✅ `figure2_error_budget.pdf` - Systematic budget comparison
- ✅ `figure4_h0_compilation.pdf` - Multi-method convergence forest plot
- ✅ Additional PNG versions and supplementary figures

---

## All Referee Feedback Addressed ✅

### 1. "9 vs 10" Inconsistencies
- **Fixed:** Eq. (1) now uses `\sum_{i=1}^{9}`
- **Fixed:** Text references "nine partially correlated sources (Table 1)"
- **Fixed:** §2.2 references "9×9 correlation matrix" and "9 eigenvalues"

### 2. Stage-4 σ_combined Inconsistency
- **Fixed:** Line 368 now correctly states σ_combined = 1.65 km/s/Mpc
- **Verified:** Table 2 shows 1.65 km/s/Mpc for Stage 4
- **Added:** Explicit calculation √(0.80² + 1.04² + 1.0²) = 1.65

### 3. Mathematical Validation Variance Values
- **Fixed:** Line 211 updated to current values:
  - σ²_SH0ES,corr = 1.19 (from σ = 1.09 km/s/Mpc)
  - σ²_ours,corr = 2.92 (from σ = 1.71 km/s/Mpc)

### 4. Metallicity Prior Baseline vs Sensitivity
- **Fixed:** Line 548 (§4.4 Limitations) now explicitly states:
  - Baseline: γ = -0.2 ± 0.1 mag/dex (Prior 1)
  - Sensitivity only: γ ≈ -0.35 (Prior 2) and γ = 0 (Prior 3)

### 5. Table 3 Outdated σ_sys
- **Fixed:** Table 3 comments updated from σ_sys = 2.45 to σ_sys,corr = 1.71 km/s/Mpc
- **Verified:** Consistent with Stage 5 correlated systematics

### 6. SNe Ia Coupling Claims
- **Fixed:** Line 200 removed false coupling claims (SNe--metal, SNe--extinction)
- **Added:** Justification that SNe Ia systematics are independent of Cepheid systematics
- **Verified:** Table correlation matrix row/column 9 has all zeros off-diagonal

### 7. Correction Scheme Harmonization
- **Fixed:** All references now explicitly state "Scenario A + Prior 1 baseline: 0 parallax -2.5 period -1.0 metallicity = -3.5 cumulative"
- **Updated:** Lines 182, 681, 725, 776, 799-804
- **Added:** MAP = -2.33 km/s/Mpc is consistent within posterior 68% CI

### 8. CCHP Independent Row Removed
- **Fixed:** Mixed-unit row deleted from Table 1 body
- **Relocated:** Information properly documented in table comments with \citep{Freedman2024}

### 9. Notation & Units Consistency
- **Verified:** All unit notation uses `km~s$^{-1}$~Mpc$^{-1}$` consistently
- **Verified:** All section references use `\S\ref{...}` format

### 10. Numeric Spot-Checks ✅
- **Stage 4:** √(0.80² + 1.04² + 1.0²) = 1.65 km/s/Mpc ✓
- **Planck-free tension:** 1.45/2.33 = 0.62σ ≈ 0.6σ ✓

### 11. Literature Pulse Check ✅
- **DESI Y1:** H₀ = 68.52 ± 0.62 km/s/Mpc (updated from 68.5 ± 0.6)
- **ACT DR6:** CMB lensing + BAO + BBN yields H₀ ≈ 68.1-68.3 ± (1.0-1.1)
- **SPT-3G:** H₀ ≈ 66.7 ± 0.6 km/s/Mpc (already correct)
- **JWST Riess et al.:** Added 2.5× scatter reduction, >8σ crowding rejection

---

## Key Baseline Values (Scenario A + Prior 1)

### Systematic Budget (9 sources)
- **Uncorrelated:** σ_sys,uncorr = 1.45 km/s/Mpc (1.4× vs SH0ES 1.04)
- **Correlated:** σ_sys,corr = 1.71 km/s/Mpc (1.6× vs SH0ES 1.09)
- **Correlation impact:** 18% increase

### Stage-wise Tension Evolution
| Stage | H₀ (km/s/Mpc) | σ_total | Tension (vs Planck) |
|-------|---------------|---------|---------------------|
| 1 | 73.17 | 0.80 | 6.0σ |
| 2 | 73.17 | 1.31 | 4.1σ |
| 3 | 73.17 | 1.31 | 4.1σ |
| 4 | 70.67 | 1.65 | 1.9σ |
| 5 | 69.67 | 1.89 | 1.2σ |

### Bias Corrections
- **Parallax (Scenario A):** 0 km/s/Mpc (adopt SH0ES internally-fitted ZP)
- **Period distribution:** -2.5 km/s/Mpc (mid-range of [-1.5, -3.5] bracket)
- **Metallicity (Prior 1):** -1.0 km/s/Mpc (γ = -0.2 ± 0.1)
- **Cumulative:** -3.5 km/s/Mpc
- **MAP estimate:** -2.33 km/s/Mpc (consistent within 68% CI)

### Late-Universe Convergence (Planck-independent)
- **JAGB + Cosmic Chronometers:** H₀ = 68.22 ± 1.36 km/s/Mpc
- **χ²_red:** 0.04 (excellent consistency)
- **Corrected Cepheid tension:** ~0.6σ from late-universe mean

---

## Compilation Instructions

### Overleaf Setup
1. Upload `manuscript_overleaf_v8.6A.zip` to Overleaf
2. Extract all files maintaining directory structure
3. Set **Main document:** `manuscript.tex`
4. Set **Compiler:** pdfLaTeX
5. **Compile sequence:** pdflatex → bibtex → pdflatex → pdflatex

### Local Compilation
```bash
pdflatex manuscript
bibtex manuscript
pdflatex manuscript
pdflatex manuscript
```

### Document Class
- **AASTeX version:** 7.01 (two-column ApJ format)
- **Journal:** Astrophysical Journal (ApJ)
- **Style:** aastex631 document class

---

## Validation Checklist

### Content
- ✅ All 11 referee feedback items addressed
- ✅ Numeric spot-checks verified
- ✅ Literature pulse check complete (DESI, ACT, SPT, JWST)
- ✅ All calculations verified and consistent

### Technical
- ✅ 9×9 correlation matrix throughout
- ✅ 9 sources in error budget
- ✅ Unit notation consistent (km~s$^{-1}$~Mpc$^{-1}$)
- ✅ Section references consistent (\S\ref{...})
- ✅ Correction scheme harmonized (0 -2.5 -1.0 = -3.5)

### Files
- ✅ All 8 tables present and updated
- ✅ All 3 main figures (PDF) included
- ✅ All supplementary figures included
- ✅ Complete bibliography with 2024-2025 citations
- ✅ README with complete instructions

### Cross-references
- ✅ All table references valid
- ✅ All figure references valid
- ✅ All equation references valid
- ✅ All section references valid
- ✅ All citations valid

---

## Key Changes Since v8.5

### Structural
- Removed covariant crowding standalone term (10 → 9 sources)
- Updated all matrix dimensions (10×10 → 9×9)
- Adopted 2025 metallicity consensus (γ = -0.2 ± 0.1 as baseline)

### Values
- **Stage 4 σ:** 1.74 → 1.65 km/s/Mpc
- **Stage 5 σ_sys,corr:** 2.45 → 1.71 km/s/Mpc
- **Uncorrelated ratio:** 2.1× → 1.4×
- **Correlated ratio:** 2.4× → 1.6×
- **DESI H₀:** 68.5 ± 0.6 → 68.52 ± 0.62 km/s/Mpc

### Framing
- Emphasized JWST shows zero offset but 2.5× scatter reduction
- Strengthened ACT DR6 CMB lensing + BAO + BBN support
- Clarified metallicity baseline vs sensitivity distinction
- Harmonized all correction scheme references

---

## Repository Information

- **GitHub:** https://github.com/awiley-intel/distance-ladder-systematics
- **Baseline Commit:** 85c56c3
- **Version:** v8.6A (M1 peer review response complete)
- **License:** Creative Commons CC-BY 4.0

---

## Contact

For questions about compilation or content, refer to the project repository or README.txt included in the package.

---

**Package Status:** ✅ READY FOR SUBMISSION
**All Referee Feedback:** ✅ INCORPORATED
**Validation:** ✅ COMPLETE
**File Size:** 4.5 MB
**Total Files:** 31 (manuscript + tables + figures + README)
