# Overleaf Submission Guide

**Date**: 2025-10-31
**Package**: `manuscript_overleaf.zip` (1.2M)
**Status**: ✅ **READY FOR UPLOAD**

---

## Package Contents (17 files)

### ✅ Manuscript Files (2)
- `manuscript/manuscript.tex` (692 lines, 86 KB) - **Updated with M1+M2 changes**
- `manuscript/references.bib` (363 lines, 12 KB)

### ✅ Figures (5)
- `figures/figure1_tension_evolution.png` (217 KB)
- `figures/figure2_error_budget.png` (303 KB) - **High-quality version**
- `figures/figure3_cchp_crossval_real.png` (305 KB)
- `figures/figure4_h0_compilation.png` (204 KB)
- `figures/figure5_h6_fit.png` (354 KB)

### ✅ Tables (7)
- `data/tables/table1_systematic_budget.tex` (1.4 KB)
- `data/tables/table2_tension_evolution.tex` (1.6 KB)
- `data/tables/table3_h0_compilation.tex` (1.5 KB)
- `data/tables/table4_cchp_crossval.tex` (1.5 KB)
- `data/tables/table5_jwst_crossvalidation.tex` (1.9 KB)
- `data/tables/table6_cosmic_chronometers.tex` (2.4 KB)
- `data/tables/table_correlation_matrix.tex` (2.4 KB) - **M1 correlation matrix**

---

## Upload Instructions

### Step 1: Go to Overleaf
Navigate to: https://www.overleaf.com

### Step 2: Create New Project
1. Click **"New Project"** button (top left)
2. Select **"Upload Project"** from dropdown
3. Click **"Select a .zip file"** button
4. Browse to and select: `manuscript_overleaf.zip`

**Location**: `/Users/awiley/Code/distance-ladder-systematics/manuscript_overleaf.zip`

### Step 3: Configure Project Settings
After upload completes:

1. **Set Compiler**:
   - Click the Overleaf menu icon (☰) in top left
   - Select **"pdfLaTeX"** as compiler

2. **Set Main Document**:
   - In same menu, set main document to: `manuscript/manuscript.tex`

3. **Click "Recompile"** button

### Step 4: Compilation Sequence
Overleaf will automatically run:
```
1. pdflatex manuscript.tex
2. bibtex manuscript
3. pdflatex manuscript.tex  (resolve citations)
4. pdflatex manuscript.tex  (resolve references)
```

**Expected time**: 30-60 seconds

---

## Post-Compilation Verification

### Critical Values to Check in PDF

**Abstract (page 1)**:
- [ ] σ_sys = 3.14 km/s/Mpc (not 2.45)
- [ ] "factor 2.7×" or "factor 2.65×"
- [ ] Tension reduces to 0.9σ

**Section 3.1 Title**:
- [ ] "Cepheid Systematic Uncertainties Underestimated by Factor 2.7×"

**Section 3.2 Title**:
- [ ] "H₀ Tension Reduced from 6.0σ to 0.9σ"

**Figure 1 Caption**:
- [ ] Stage 5: σ_sys = 3.14 km/s/Mpc
- [ ] Final tension: 0.9σ
- [ ] Factor 7.0× reduction

**Equation on page ~X** (σ_sys,corr formula):
- [ ] Shows √(ΣᵢΣⱼ σᵢσⱼRᵢⱼ) = 3.14 km/s/Mpc

---

## Known Placeholders (Optional to Edit)

These can be left as-is for reviewer submission or filled in:

**Author Information** (lines 26-30):
```latex
\author[0000-0000-0000-0000]{[Your Name]}
\affil{[Your Institution]}
\email{[Your Email]}
```

**Acknowledgments** (line ~454):
```latex
[Institution] for computational resources
```

**Code Repository** (line ~461):
```latex
[GitHub repository URL]
```

**Note**: You can compile with placeholders - they won't prevent PDF generation.

---

## If Compilation Fails

### Common Issues:

**1. Missing Files Error**
- Check that all 5 figures and 7 tables loaded correctly
- Verify file paths in manuscript.tex match zip structure

**2. Bibliography Error**
- Ensure `references.bib` is in `manuscript/` folder
- Check that bibtex ran successfully (see compilation log)

**3. Package/Font Errors**
- Overleaf should have all AASTeX 6.31 packages
- If missing, add to preamble or contact Overleaf support

**4. Path Issues**
- All `\input{}` and `\includegraphics{}` use relative paths from manuscript/
- Example: `\input{../data/tables/table1...}` goes up one level

---

## After Successful Compilation

### Download PDF
1. Click **"Download PDF"** button (top right, near Recompile)
2. Save as: `Forensic_Analysis_Distance_Ladder_Systematics_v1.pdf`

### Replace Old PDF
```bash
# In your local repository
cd /Users/awiley/Code/distance-ladder-systematics
mv ~/Downloads/manuscript.pdf Forensic_Analysis_Distance_Ladder_Systematics_v1.pdf
```

### Verify Locally
Open the downloaded PDF and check the verification checklist above.

---

## M1+M2 Changes Summary (What's New)

### M1 (Correlated Systematics)
- ✅ σ_sys increased from 2.45 → 3.14 km/s/Mpc
- ✅ Ratio increased from 2.36× → 2.65×
- ✅ Tension reduced from 1.07σ → 0.86σ (rounds to 0.9σ)
- ✅ Added correlation matrix table
- ✅ Updated Abstract, §3.1, §3.2, Figure 1 caption

### M2 (Bias Corrections)
- ✅ Three derivation boxes (parallax, period, metallicity)
- ✅ Joint Bayesian forward propagation (Appendix A)
- ✅ Sign convention: ΔH₀ ≡ H₀^corrected - H₀^SH0ES < 0
- ✅ M1 vs M2 reconciliation paragraph
- ✅ Period histogram figure
- ✅ Sensitivity analysis sentences

**All changes are in the LaTeX source** - this compilation will produce the correct PDF.

---

## Timeline

- **M1 Implementation**: Oct 27-28
- **M2 Implementation**: Oct 28-29
- **Figure 1 Caption Fix**: Oct 31
- **Package Creation**: Oct 31, 22:21
- **Next**: Upload to Overleaf and recompile

---

## Submission Checklist

Before submitting to journal:

- [ ] PDF compiled successfully on Overleaf
- [ ] All critical values verified (see checklist above)
- [ ] Author information filled in (or left as placeholders)
- [ ] PDF downloaded and saved locally
- [ ] Old PDF (v0) archived/removed
- [ ] Final PDF ready for journal submission

---

**Package Location**: `/Users/awiley/Code/distance-ladder-systematics/manuscript_overleaf.zip`

**Ready to upload!** 🚀