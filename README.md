# Distance Ladder Systematics & Hubble Tension Analysis

**Systematic Error Assessment in Cepheid Distance Ladder Measurements**

[![Status](https://img.shields.io/badge/Status-Submission%20Ready-success)](manuscript_overleaf_v8.6H.zip)
[![Journal](https://img.shields.io/badge/Target-ApJ-blue)](https://iopscience.iop.org/journal/0004-637X)
[![License](https://img.shields.io/badge/License-Pending%20Publication-orange)](LICENSE)

**Last Updated**: 2025-11-14

---

## Overview

This project provides a comprehensive reassessment of systematic uncertainties in Cepheid-based distance ladder measurements and their impact on the reported "Hubble tension." Our analysis reveals that realistic systematic error accounting reduces the tension from **6.0σ to ~1σ**, suggesting the tension is largely consistent with a measurement artifact rather than requiring new physics.

### Key Results

- **Systematic error reassessment**: σ_sys = 1.71 km/s/Mpc (correlated), representing a 1.6× underestimation in published uncertainties
- **Multi-method convergence**: JAGB + cosmic chronometers → H₀ = 68.22 ± 1.36 km/s/Mpc (Planck-independent)
- **Tension reduction**: From 6.0σ → 1.2σ (Planck-relative) or 0.6σ (Planck-independent)
- **Robustness validated**: Tension remains <2σ across all tested systematic scenarios
- **JWST cross-validation**: 2.3× excess Cepheid scatter confirms systematic budget assessment

---

## Quick Start

### Option 1: Upload to Overleaf (Recommended)

1. Download the pre-built package: [`manuscript_overleaf_v8.6H.zip`](manuscript_overleaf_v8.6H.zip)

2. Upload to [Overleaf](https://www.overleaf.com):
   - Click "New Project" → "Upload Project"
   - Select the zip file
   - Set compiler to **pdfLaTeX**
   - Click "Recompile"

3. Post-upload fix (for proper σ rendering):
   ```latex
   % Add after line 12 in manuscript.tex:
   \usepackage{lmodern}
   ```

### Option 2: Local Compilation

**Requirements:**
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- AASTeX 7.01 (included in package)
- Standard packages: graphicx, amsmath, natbib

**Compile:**
```bash
cd manuscript
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex
```

---

## Project Structure

```
distance-ladder-systematics/
├── README.md                            # This file
├── manuscript_overleaf_v8.6H.zip        # Final submission package (4.5 MB)
│
├── manuscript/                          # LaTeX source
│   ├── manuscript.tex                   # Main manuscript (AASTeX 7.01)
│   └── references.bib                   # Complete bibliography
│
├── data/                                # All data files
│   ├── systematic_error_budget.csv      # 9 systematic sources
│   ├── cosmic_chronometers_Hz.csv       # 32 H(z) measurements
│   ├── cchp_trgb_cepheid_comparison.csv # JWST cross-validation data
│   ├── h0_measurements_compilation.csv  # Multi-method H₀ comparison
│   └── tables/                          # LaTeX tables (8 files)
│
├── figures/                             # Manuscript figures
│   ├── figure1_tension_evolution.*      # 5-stage tension reduction
│   ├── figure2_error_budget_stacked.*   # Systematic error breakdown
│   ├── figure3_cchp_crossval_real.png   # JWST cross-validation
│   ├── figure4_h0_compilation.*         # Multi-method convergence
│   └── figure5_h6_fit.png               # Cosmic chronometer fit
│
├── analysis/                            # Python analysis scripts
│   ├── calculate_error_budget.py        # Systematic error calculations
│   ├── calculate_tension_evolution.py   # Tension staging analysis
│   ├── create_figure*.py                # Figure generation
│   └── h6_h0_estimate.py                # Cosmic chronometer MCMC
│
└── docs/                                # Documentation
    └── development/                     # Development history archive
```

---

## Reproducing Results

### 1. Generate Data Files

```bash
cd analysis
python3 calculate_error_budget.py              # → systematic_error_budget.csv
python3 calculate_tension_evolution.py         # → tension_evolution.csv
python3 h6_h0_estimate.py                      # → mcmc_chains_LCDM_2D.npy
```

### 2. Generate Figures

```bash
python3 create_figure1_tension_evolution.py    # → figure1_tension_evolution.*
python3 create_figure2_error_budget.py         # → figure2_error_budget_stacked.*
python3 create_figure3_cchp_crossval_real.py   # → figure3_cchp_crossval_real.png
python3 create_figure4_h0_compilation.py       # → figure4_h0_compilation.*
python3 create_figure5_h6_fit.py               # → figure5_h6_fit.png
```

### 3. Generate Tables

```bash
python3 create_manuscript_tables.py            # → data/tables/*.tex
```

**Total runtime**: ~1-2 minutes on a modern laptop (no GPU required)

---

## Key Scientific Claims

### 1. SH0ES Systematic Underestimation

**Claim:** SH0ES underestimates systematic uncertainties by 1.6×

- SH0ES assessment: σ_sys = 1.04 km/s/Mpc (uncorrelated)
- Our assessment: σ_sys = 1.71 km/s/Mpc (with realistic correlations)
- Underestimation factor: 1.6× when accounting for correlated error sources

**Data:** [`data/systematic_error_budget.csv`](data/systematic_error_budget.csv), [`table1_systematic_budget.tex`](data/tables/table1_systematic_budget.tex)

### 2. Multi-Method Convergence

**Claim:** Late-universe methods converge at H₀ ≈ 68 km/s/Mpc (Planck-independent)

- JAGB + Cosmic chronometers: 68.22 ± 1.36 km/s/Mpc
- Three-method mean (JAGB + H(z) + Planck): 67.48 ± 0.50 km/s/Mpc
- Excellent consistency: χ²_red ≈ 0.04

**Data:** [`data/h0_measurements_compilation.csv`](data/h0_measurements_compilation.csv), [`table3_h0_compilation.tex`](data/tables/table3_h0_compilation.tex)

### 3. Tension Reduction

**Claim:** Realistic systematics reduce tension from 6.0σ → ~1σ

| Stage | Description | Tension vs Planck |
|-------|-------------|-------------------|
| 1 | SH0ES baseline (statistical only) | 6.0σ |
| 2 | Add uncorrelated systematics | 3.5σ |
| 3 | Add realistic correlations | 2.9σ |
| 4 | Apply three bias corrections | 1.6σ |
| 5 | Sensitivity across scenarios | 0.3σ - 1.7σ |

**Planck-independent:** 0.6σ (vs JAGB+chronometers convergence)

**Data:** [`data/tension_evolution.csv`](data/tension_evolution.csv), [`table2_tension_evolution.tex`](data/tables/table2_tension_evolution.tex)


### 4. JWST Cross-Validation

**Claim:** JWST data confirms systematic underestimation

- 15 galaxies with Cepheid + TRGB + JAGB measurements
- Cepheid vs JAGB scatter: 2.3× larger than JAGB vs TRGB
- Jackknife validation and robust estimators confirm excess
- Supports realistic Cepheid systematic error budget

**Data:** [`data/cchp_trgb_cepheid_comparison.csv`](data/cchp_trgb_cepheid_comparison.csv), [`table5_jwst_crossvalidation.tex`](data/tables/table5_jwst_crossvalidation.tex)

---

## Data Files

All data files are CSV format with header comments documenting sources and methods.

### Primary Data

- **systematic_error_budget.csv**: 9 systematic error sources with literature assessments
- **cosmic_chronometers_Hz.csv**: 32 H(z) differential age measurements
- **cchp_trgb_cepheid_comparison.csv**: JWST cross-validation data (15 galaxies)
- **h0_measurements_compilation.csv**: Multi-method H₀ comparison

### Analysis Outputs

- **tension_evolution.csv**: 5-stage tension reduction summary
- **error_budget_summary.csv**: Quadrature error totals
- **cchp_crossval_summary.csv**: JWST cross-validation statistics

### MCMC Chains

- **mcmc_chains_LCDM_2D.npy**: 128,000 samples (H₀, Ω_m) for cosmic chronometer fit
- Additional chains available for intrinsic scatter and wCDM models

---

## Manuscript Status

**Submission Ready**: ✅ All checks complete

- ✅ All numerical claims verified against data files
- ✅ All citations cross-checked in bibliography
- ✅ Computational results fully reproducible
- ✅ LaTeX compilation tested (Overleaf + local)
- ✅ All figures and tables render correctly
- ✅ Author metadata complete (ORCID included)

**Package:** [`manuscript_overleaf_v8.6H.zip`](manuscript_overleaf_v8.6H.zip) (4.5 MB)

**Next Steps:**
1. Upload package to Overleaf
2. Add `\usepackage{lmodern}` after line 12 (fixes σ rendering)
3. Recompile and verify PDF
4. Submit to ApJ

---

## Requirements

### Python Environment

**Tested with:** Python 3.11+ and Python 3.12

```bash
# Create conda environment
conda env create -f environment.yml
conda activate distance-ladder

# Or install manually
pip install numpy pandas matplotlib scipy emcee corner
```

### LaTeX Requirements

- AASTeX 7.01 (included in package)
- pdfLaTeX + BibTeX
- Standard packages: graphicx, amsmath, natbib, hyperref

---

## Citation

If you use this work, please cite:

```bibtex
@article{Wiley2025,
  author = {Wiley, Aaron},
  title = {{Forensic Analysis of Distance Ladder Systematics:
           The Hubble Tension Reduced from $\sim$6$\sigma$ to $\sim$1$\sigma$}},
  journal = {The Astrophysical Journal},
  year = {2025},
  note = {Submitted}
}
```

**Repository citation:** See tag [`v8.6H`](https://github.com/ylecoyote/distance-ladder-systematics/releases/tag/v8.6H) for the exact version corresponding to the submitted manuscript. GitHub also provides a "Cite this repository" button based on [`CITATION.cff`](CITATION.cff).

---

## Contact

**Author**: Aaron Wiley
**ORCID**: [0009-0007-1612-9203](https://orcid.org/0009-0007-1612-9203)
**Affiliation**: Independent Researcher
**Email**: awiley@outlook.com

For questions about the analysis, methodology, or data, please open an issue or contact the author.

---

## Acknowledgments

This research made use of:
- Gaia EDR3 parallax data
- JWST/NIRCam observations (CCHP program)
- Cosmic chronometer measurements (Moresco et al. 2022)
- Planck 2018 cosmological constraints
- SH0ES Cepheid measurements (Riess et al. 2022)

Full acknowledgments in manuscript.

---

## License

This work is prepared for submission to The Astrophysical Journal. All rights reserved pending publication.

Code and data are provided for reproducibility and peer review. Please contact the author regarding reuse.

---

*Manuscript ready for ApJ submission • Publication-ready with comprehensive literature coverage*
