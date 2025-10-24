# Quick Start Guide - Overleaf Upload

## 🚀 Fastest Path to PDF (10 Minutes)

### Step 1: Upload to Overleaf (5 min)

1. **Go to**: https://www.overleaf.com
2. **Click**: "New Project" → "Upload Project"
3. **Upload**: `manuscript_overleaf.zip` (584 KB)
4. **Wait**: For upload to complete

### Step 2: Configure Project (2 min)

In Overleaf project settings:

- **Compiler**: pdfLaTeX (from dropdown)
- **Main document**: `manuscript/manuscript.tex`

### Step 3: Compile (3 min)

1. **Click**: "Recompile" button
2. **Wait**: For 4-stage compilation:
   - Run 1: pdflatex (generates .aux)
   - Run 2: bibtex (processes citations)
   - Run 3: pdflatex (resolves citations)
   - Run 4: pdflatex (finalizes)
3. **Result**: `manuscript.pdf` appears in viewer

### Step 4: Review PDF

Check that all content renders correctly:

- ✓ Title, author (Aaron Wiley)
- ✓ Abstract (205 words)
- ✓ All section headings
- ✓ 5 figures appear
- ✓ 4 tables appear
- ✓ Citations render as (Author Year)
- ✓ References section populated

---

## ⚠️ One Remaining Placeholder

**GitHub URL** appears as:
```
https://github.com/[username]/distance-ladder-systematics
```

**To fix**:
1. In Overleaf, find lines 458 and 467
2. Replace `[username]` with your GitHub username
3. Or leave as-is for initial review

---

## 📝 If Compilation Fails

### Error: "Cannot find aastex7.cls"

**Fix**: Overleaf should have this by default. If not:
- Menu → Settings → TeX Live version → Use latest

### Error: "Cannot find figure file"

**Fix**: Check figure paths in manuscript.tex lines 476-517:
```latex
\includegraphics[width=\textwidth]{../figures/figure1_tension_evolution.png}
```

If error persists, change to:
```latex
\includegraphics[width=\textwidth]{figures/figure1_tension_evolution.png}
```

### Error: "Undefined citation"

**Fix**: Run full compilation sequence (Recompile button does this automatically)

---

## 📊 What You'll See

### Abstract
```
The "Hubble tension"—a 5-6σ discrepancy between local distance
ladder (H₀ = 73.17 ± 0.86 km/s/Mpc, Riess et al. 2022) and Planck
CMB measurements...
```

### Key Results
- Factor 2.4× systematic underestimate found
- H₀ tension reduced from 6.0σ → 1.1σ
- Three methods converge at H₀ = 67.48 ± 0.50 km/s/Mpc

### Figures (5 total)
1. Tension evolution (5 stages)
2. Error budget comparison (high-quality)
3. CCHP cross-validation (high-quality)
4. H₀ compilation forest plot
5. Cosmic chronometer H(z) fit

### Tables (4 total)
1. Systematic error budget (11 sources)
2. Tension evolution (5 stages)
3. H₀ measurements compilation
4. CCHP cross-validation results

---

## ✅ Success Criteria

PDF should be:
- ✓ ~20-25 pages (two-column ApJ format)
- ✓ All figures visible
- ✓ All tables formatted correctly
- ✓ No "??" in citations
- ✓ References section complete (28 entries)
- ✓ No compilation errors in Overleaf log

---

## 🎯 Next Steps After PDF Review

1. **Optional**: Replace placeholder figures (1, 4, 5) with high-quality versions
2. **Optional**: Add specific arXiv number for Anderson2024 reference
3. **Ready**: Download PDF for final proofreading
4. **Submit**: Upload to ApJ submission system

---

## 📧 Submission to ApJ

When ready to submit:

1. **Go to**: https://apj-submit.aas.org
2. **Create account** (if needed)
3. **New submission**:
   - Manuscript type: Research Article
   - Topic: Cosmology, Distance Scale
   - Upload: manuscript.tex, references.bib, figures/, tables/
4. **Suggested keywords**: Hubble constant, Cepheid variables, Systematic errors, Distance scale
5. **Cover letter**:
   - Explain novel contribution (forensic systematic analysis)
   - Highlight key finding (tension reduction 6σ → 1σ)
   - Suggest reviewers (optional)

---

## 📚 Full Documentation

For detailed help, see:
- [SUBMISSION_READY.md](SUBMISSION_READY.md) - Complete checklist
- [LATEX_COMPILATION_GUIDE.md](docs/LATEX_COMPILATION_GUIDE.md) - Compilation troubleshooting
- [COMPILATION_STATUS.md](COMPILATION_STATUS.md) - File status

---

**Estimated time from here to submission**: 1-3 hours

**Good luck with your submission!** 🚀
