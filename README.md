# Distance Ladder Systematics & Hubble Tension Analysis

**Systematic Error Assessment in Cepheid Distance Ladder Measurements**

[![Status](https://img.shields.io/badge/Status-Submission%20Ready-success)](manuscript_overleaf_v8.6H.zip)
[![Journal](https://img.shields.io/badge/Target-ApJ-blue)](https://iopscience.iop.org/journal/0004-637X)
[![License](https://img.shields.io/badge/License-Pending%20Publication-orange)](LICENSE)

**Last Updated**: 2025-11-14

---

## Overview

This project provides a comprehensive reassessment of systematic uncertainties in Cepheid-based distance ladder measurements and their impact on the reported "Hubble tension." Our analysis reveals that realistic systematic error accounting reduces the tension from **~6.0σ to ~1σ**, suggesting the tension is largely consistent with a measurement artifact rather than requiring new physics.

For full technical details, see [`manuscript.tex`](manuscript/manuscript.tex) and the data/figures listed below.

### Key Results

- **Systematic error reassessment**: σ_sys = 1.71 km/s/Mpc (correlated), representing a 1.6× underestimation in published uncertainties
- **Multi-method convergence**: JAGB + cosmic chronometers → H₀ = 68.22 ± 1.36 km/s/Mpc (Planck-independent)
- **Tension reduction**: From ~6.0σ → 1.2σ (Planck-relative) or 0.6σ (Planck-independent)
- **Robustness validated**: Tension remains <2σ across all tested systematic scenarios
- **JWST cross-validation**: TRGB–JAGB RMS ≈ 0.048 mag vs. Cepheid–TRGB RMS ≈ 0.108 mag (~2.3× larger), confirming the enlarged Cepheid systematic budget

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
- AASTeX (class file and support files included in the package)
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

## Project structure

- `analysis/` – Python scripts for error budgets, tension evolution, MCMC fits, robustness tests, and figure/table generation
- `data/` – Input and generated data products:
  - `systematic_error_budget.csv`, `tension_evolution.csv`, `h0_measurements_compilation.csv`, etc.
  - `cchp_trgb_cepheid_comparison.csv`, `cchp_trgb_jagb_comparison.csv`, and JWST robustness results
  - `tables/` – LaTeX table fragments written by `analysis/create_manuscript_tables.py`
- `figures/` – Output figures for the manuscript (PDF + PNG for Figs. 1–5 and auxiliary plots)
- `manuscript/` – LaTeX source (`manuscript.tex`), class file, BibTeX, and LaTeX logs
- `overleaf_package_final/` – Final Overleaf-ready package for v8.6H (mirrors `manuscript/` + `figures/` + `tables/`)
- `logs/` – JSON and run logs from analysis/validation sessions (not required to reproduce results)
- `_tmp/` – Archived drafts, peer-review notes, AI review logs, and historical Overleaf packages (not needed for reproduction)
- `docs/` – Development notes (internal); see `_tmp/` for historical validation and review documents
- `environment.yml` – Reproducible Python environment specification

---

## Reproducing results

All commands below assume you have created/activated the project environment (see `environment.yml`) and are running from the repository root.

### 1. Generate data files

```bash
python3 analysis/calculate_error_budget.py              # → data/systematic_error_budget.csv, data/systematic_budget_recalculated.csv
python3 analysis/calculate_tension_evolution.py         # → data/tension_evolution.csv
python3 analysis/h6_h0_estimate.py                      # → data/mcmc_chains_LCDM_2D.npy
python3 analysis/cosmic_chronometer_fit_random_effects.py  # → data/cosmic_chronometer_random_effects_results.csv

```

### 2. Generate figures

```bash
python3 analysis/create_figure1_tension_evolution.py    # → figures/figure1_tension_evolution.*
python3 analysis/create_figure2_error_budget.py         # → figures/figure2_error_budget_stacked.png
python3 analysis/create_figure3_cchp_crossval_real.py   # → figures/figure3_cchp_crossval_real.*
python3 analysis/create_figure4_h0_compilation.py       # → figures/figure4_h0_compilation.*
python3 analysis/create_figure5_hz_fit_intrinsic_scatter.py  # → figures/figure5_h6_fit.png
```

### 3. Generate tables

```bash
python3 analysis/create_manuscript_tables.py            # → data/tables/*.tex
```

**Total runtime:** ~1–2 minutes on a modern laptop (no GPU required).

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

See Fig. 1 and Table 2 in the manuscript for the full staged tension-evolution visualization.

**Data:** [`data/tension_evolution.csv`](data/tension_evolution.csv), [`table2_tension_evolution.tex`](data/tables/table2_tension_evolution.tex)

### 4. JWST Cross-Validation

**Claim:** JWST data confirms systematic underestimation

- 15 galaxies with Cepheid + TRGB + JAGB measurements
- TRGB–JAGB agreement: RMS ≈ 0.048 mag with ≈0 mean offset
- Cepheid–TRGB scatter: RMS ≈ 0.108 mag (~2.3× larger than TRGB–JAGB)
- Jackknife validation and robust estimators confirm this excess
- Supports a larger Cepheid systematic error budget rather than JWST-limited photometry

See Fig. 3 and Table 5 in the manuscript for the full cross-validation comparison.

**Data:** [`data/cchp_trgb_cepheid_comparison.csv`](data/cchp_trgb_cepheid_comparison.csv), [`table5_jwst_crossvalidation.tex`](data/tables/table5_jwst_crossvalidation.tex)

---

## Data files

All data files are CSV (or NPZ/Numpy) format with header comments documenting sources and methods.

### Primary data

- [`data/systematic_error_budget.csv`](data/systematic_error_budget.csv): 9 Cepheid systematic error sources with quadrature totals  
- [`data/hierarchical_hz_results.csv`](data/hierarchical_hz_results.csv): 32 H(z) differential age measurements and best-fit hierarchical CC model values  
- [`data/cchp_trgb_cepheid_comparison.csv`](data/cchp_trgb_cepheid_comparison.csv): JWST CCHP Cepheid vs TRGB distances (per galaxy)  
- [`data/cchp_trgb_jagb_comparison.csv`](data/cchp_trgb_jagb_comparison.csv): JWST CCHP JAGB vs TRGB distances (per galaxy)  
- [`data/h0_measurements_compilation.csv`](data/h0_measurements_compilation.csv): Multi-method H₀ comparison (Cepheid, JAGB, CC, Planck, etc.)

### Analysis outputs

- [`data/tension_evolution.csv`](data/tension_evolution.csv): 5-stage H₀ tension reduction summary  
- [`data/cchp_crossval_summary.csv`](data/cchp_crossval_summary.csv): JWST cross-validation statistics  
- [`data/systematic_budget_recalculated.csv`](data/systematic_budget_recalculated.csv): Revised systematic budget under updated assumptions  
- [`data/cosmic_chronometer_random_effects_results.csv`](data/cosmic_chronometer_random_effects_results.csv): Random-effects CC fit summary  
- [`data/extended_correlation_sensitivity_results.csv`](data/extended_correlation_sensitivity_results.csv): Correlation-sensitivity sweep results  

### MCMC chains

- `data/mcmc_chains_LCDM_2D.npy`: 128,000 (H₀, Ωₘ) samples for the baseline LCDM CC fit  
  *(generated by `analysis/h6_h0_estimate.py`; see “Reproducing results” below)*  

Additional hierarchical and intrinsic-scatter summaries:

- [`data/hierarchical_hyperpriors.csv`](data/hierarchical_hyperpriors.csv)  
- [`data/hierarchical_hz_results.csv`](data/hierarchical_hz_results.csv)

### Manuscript tables (LaTeX)

Generated by `analysis/create_manuscript_tables.py` and used directly in the manuscript:

- `data/tables/table1_systematic_budget.tex`: Systematic error budget  
- `data/tables/table2_tension_evolution.tex`: H₀ tension staging  
- `data/tables/table3_h0_compilation.tex`: Multi-method H₀ compilation  
- `data/tables/table4_cchp_crossval.tex`: JWST CCHP cross-validation summary  
- `data/tables/table5_jwst_crossvalidation.tex`: JWST scatter statistics (TRGB/JAGB/Cepheid)  
- `data/tables/table6_cosmic_chronometers.tex`: Cosmic chronometer H(z) summary and derived H₀ constraints  
- `data/tables/table_anchor_weights.tex`: Anchor weighting scheme  
- `data/tables/table_correlation_matrix.tex`: Systematic correlation matrix  

---

## Manuscript Status

✅ Submission-ready for ApJ (version v8.6H):
- ✅ All numerical claims verified against data files
- ✅ All citations cross-checked in bibliography
- ✅ Computational results fully reproducible
- ✅ LaTeX compilation tested (Overleaf + local)
- ✅ All figures and tables render correctly
- ✅ Author metadata complete (ORCID included)

See [`docs/MANUSCRIPT_STATUS.md`](docs/MANUSCRIPT_STATUS.md) for validation details.

**Package:** [`manuscript_overleaf_v8.6H.zip`](manuscript_overleaf_v8.6H.zip) (4.5 MB)

**Submission:**  
Package `manuscript_overleaf_v8.6H.zip` has been tested on Overleaf and is ready for ApJ submission.

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

See LICENSE for full pre-publication terms.

---

*Manuscript ready for ApJ submission • Publication-ready with comprehensive literature coverage*
