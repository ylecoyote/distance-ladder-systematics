# Data Provenance and External Sources

This document tracks all external datasets, their sources, retrieval dates, and citations used in this analysis. All data processing and derivation steps are documented to ensure complete reproducibility.

**Last Updated:** 2026-04-03
**Analysis Version:** v8.9
**Branch:** main

---

## 1. Cosmic Chronometer Measurements (H(z) Data)

### Source
Compilation of differential galaxy age measurements providing distance-independent H(z) constraints.

**Primary References:**
- Moresco et al. (2012, JCAP, 7, 53) - "Improved constraints on the expansion rate of the Universe"
- Moresco et al. (2016, JCAP, 5, 14) - "A 6% measurement of the Hubble parameter"
- Zhang et al. (2014, RAA, 14, 1221) - "Four new observational H(z) data"
- Simon et al. (2005, PhRvD, 71, 123001) - "Constraints on the redshift dependence"
- Stern et al. (2010, JCAP, 2, 8) - "Cosmic chronometers"

**File Location:** `data/cosmic_chronometers_Hz.csv` (mirrored for self-contained reproducibility)
- Original source: pcm-exploration repository (copied 2025-11-18)
- Fallback paths: External pcm-exploration locations (if local copy unavailable)

**Data Structure:**
```
Columns: z, Hz, sigma_Hz
Format: CSV with comment header
N_measurements: 32
Redshift range: 0.07 ≤ z ≤ 1.965
```

**Retrieval Date:** 2025-11 (compilation from literature)

**Processing:**
- Used in: `analysis/create_figure5_hz_fit_intrinsic_scatter.py`
- Fit to ΛCDM model with Ωₘ = 0.315 (Planck 2018)
- Result: H₀ = 68.33 ± 1.57 km/s/Mpc (flat ΛCDM)

**Citation:**
```bibtex
@article{Moresco2016,
  author = {Moresco, M. and others},
  title = {A 6\% measurement of the Hubble parameter at z ∼ 0.45},
  journal = {JCAP},
  year = {2016},
  volume = {5},
  pages = {014}
}
```

---

## 2. SH0ES Cepheid Distance Ladder

### Source
Supernova H0 for the Equation of State (SH0ES) project Cepheid-calibrated distance ladder.

**Primary Reference:**
- Riess et al. (2022, ApJL, 934, L7) - "A Comprehensive Measurement of the Local Value of the Hubble Constant"

**Data Values Used:**
- H₀ = 73.04 ± 1.04 km/s/Mpc (statistical + systematic combined)
- σ_stat = 0.80 km/s/Mpc
- σ_sys = 1.04 km/s/Mpc (uncorrelated SH0ES budget)

**File:** `data/h0_measurements_compilation.csv`

**Retrieval Date:** 2022-07-11 (publication date)

**Citation:**
```bibtex
@article{Riess2022,
  author = {Riess, A.~G. and others},
  title = {A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km s$^{-1}$ Mpc$^{-1}$ Uncertainty from the Hubble Space Telescope and the SH0ES Team},
  journal = {ApJL},
  year = {2022},
  volume = {934},
  pages = {L7}
}
```

---

## 3. TRGB Distance Measurements

### Source
Tip of the Red Giant Branch distance ladder measurements.

**Primary Reference:**
- Freedman et al. (2025a) - "The Carnegie-Chicago Hubble Program"

**Data Values Used:**
- H₀ = 69.85 ± 2.33 km/s/Mpc

**File:** `data/h0_measurements_compilation.csv`

**Retrieval Date:** 2025-01 (preprint)

**Citation:**
```bibtex
@article{Freedman2025a,
  author = {Freedman, W.~L. and others},
  title = {The Carnegie-Chicago Hubble Program},
  journal = {ApJ},
  year = {2025},
  note = {in press}
}
```

**Future Update:** Once final ApJ reference is published, update with volume/page details and remove "in press" note.

---

## 4. JAGB Distance Measurements

### Source
J-region Asymptotic Giant Branch distance indicator.

**Primary Reference:**
- Freedman et al. (2025a) - "The Carnegie-Chicago Hubble Program"

**Data Values Used:**
- H₀ = 67.96 ± 2.65 km/s/Mpc

**File:** `data/h0_measurements_compilation.csv`

**Retrieval Date:** 2025-01 (preprint)

**Citation:** Same as TRGB (Freedman2025a)

---

## 5. Planck CMB Measurements

### Source
Planck 2018 cosmic microwave background analysis assuming ΛCDM.

**Primary Reference:**
- Planck Collaboration (2020, A&A, 641, A6) - "Planck 2018 results. VI. Cosmological parameters"

**Data Values Used:**
- H₀ = 67.36 ± 0.54 km/s/Mpc
- Ωₘ = 0.315 ± 0.007

**File:** `data/h0_measurements_compilation.csv`

**Retrieval Date:** 2020-09-13 (publication date)

**Citation:**
```bibtex
@article{Planck2018,
  author = {{Planck Collaboration}},
  title = {Planck 2018 results. VI. Cosmological parameters},
  journal = {A\&A},
  year = {2020},
  volume = {641},
  pages = {A6}
}
```

---

## 6. Systematic Error Budget Components

### Source
Derived from SH0ES systematic error budget with literature-informed correlations.

**Primary References:**
- Riess et al. (2022) - SH0ES systematic budget
- Anderson (2016, MNRAS, 463, 1707) - Metallicity calibrations
- Freedman (2011, ApJ, 758, 24) - HST Key Project metallicity
- Macri (2015, AJ, 149, 117) - Bandpass dependencies
- Riess (2016, ApJ, 826, 56) - Period-luminosity relations

**Files:**
- `data/systematic_error_budget.csv` - Original 10-term budget
- `data/systematic_budget_recalculated.csv` - 9-term budget (crowding covariance removed)
- `data/correlation_matrix_updated.csv` - 9×9 correlation structure

**Systematic Terms (9 components, our assessment, Scenario A + Prior 1):**
1. Parallax Zero Point: 0.30 km/s/Mpc
2. Period Distribution: 1.00 km/s/Mpc
3. Metallicity Correction: 0.50 km/s/Mpc (Prior 1: γ = -0.2 ± 0.1)
4. Crowding Direct: 0.30 km/s/Mpc
5. Photometric Calibration: 0.30 km/s/Mpc
6. Extinction/Reddening: 0.50 km/s/Mpc
7. LMC Distance: 0.20 km/s/Mpc
8. NGC4258 Distance: 0.20 km/s/Mpc
9. SNe Ia Standardization: 0.50 km/s/Mpc

**Key Correlations:**
- Metallicity ↔ Extinction: ρ = 0.3
- Period ↔ Metallicity: ρ = 0.3
- Crowding ↔ Extinction: ρ = 0.3
- Metallicity ↔ SNe Ia: ρ = 0.2
- Photometry ↔ Extinction: ρ = 0.2
- Extinction ↔ SNe Ia: ρ = 0.15

**Processing:**
- Covariance matrix propagation: Σ = diag(σ) × ρ × diag(σ)
- Resulting σ_sys,corr = 1.71 km/s/Mpc (baseline Scenario A + Prior 1)
- Off-diagonal contributes 28% of variance, inflates uncertainty by 18%

**File Creation Date:** 2025-11-14 (this work)

**Literature Justification:**
Documented in `data/correlation_matrix_literature_justification.csv`

---

## 7. Bias Corrections

### Period Distribution Correction

**Magnitude:** -2.5 km/s/Mpc (mid-range of [-1.5, -3.5] bracket)

**Uncertainty:** ±1.0 km/s/Mpc

**Source:**
Derived from period distribution mismatch between NGC4258/LMC anchors and SN host galaxies.

**References:**
- Macri et al. (2015, AJ, 149, 117) - Period-luminosity slope variations
- Riess et al. (2016, ApJ, 826, 56) - Host galaxy period distributions

**Robustness Checks:**
- Bandpass sensitivity: <0.3 km/s/Mpc variation across NIR/optical
- Selection effects: Stable under propensity-weight resampling

**File:** Derived in manuscript text (§4.3), values in `data/tension_evolution.csv`

### Metallicity Correction

**Magnitude:** -1.0 km/s/Mpc (Prior 1: consensus baseline)

**Uncertainty:** Absorbed into correlated systematic budget

**Prior 1 Specification:**
- γ = -0.2 ± 0.1 mag/dex
- Synthesizes: Riess2022, Freedman2025a (JWST/NIRCam), Freedman2001
- Narrower than SH0ES range (-0.2 to -0.5 mag/dex)

**File:** Derived in manuscript text (§4.4), values in `data/tension_evolution.csv`

---

## 8. Tension Evolution Data

### Source
Calculated values showing progressive reduction through 5 stages.

**File:** `data/tension_evolution.csv`

**Columns:**
```
Stage, H0_km_s_Mpc, Sigma_total, Tension_vs_Planck, Description
```

**Key Results (Scenario A + Prior 1 baseline):**
- Stage 1: 73.04 ± 0.80 km/s/Mpc → 5.9σ (stat only)
- Stage 2: 73.04 ± 1.31 km/s/Mpc → 4.0σ (quoted SH0ES systematic budget + stat.)
- Stage 3: 73.04 ± 1.31 km/s/Mpc → 4.0σ (Scenario A ZP)
- Stage 4: 70.54 ± 1.65 km/s/Mpc → 1.8σ (+ period correction)
- Stage 5: 69.54 ± 1.89 km/s/Mpc → 1.1σ (+ metallicity + corr. sys.)

**Tension Calculation:**
```
T = |H₀_Cepheid - H₀_Planck| / √(σ²_Cepheid + σ²_Planck)
  = |69.54 - 67.36| / √(1.89² + 0.54²)
  = 2.18 / 1.96
  = 1.11σ (rounds to 1.1σ)
```

**File Creation Date:** 2025-11-14 (this work)

---

## 9. H₀ Compilation and Convergence

### Source
Inverse-variance weighted averages of independent methods.

**File:** `data/h0_measurements_compilation.csv`

**Three-Method Convergence (JAGB + Cosmic Chron. + Planck):**
- H₀ = 67.48 ± 0.50 km/s/Mpc
- χ²_red = 0.19 (excellent consistency)
- Methods share no systematics

**Planck-Independent (JAGB + Cosmic Chron. only):**
- H₀ = 68.22 ± 1.36 km/s/Mpc
- χ²_red ≈ 0.02 (very good agreement)
- Bypasses early-universe physics

**Corrected Cepheid vs. Planck-Independent:**
- Difference: 69.54 - 68.22 = 1.32 km/s/Mpc
- Combined uncertainty: √(1.89² + 1.36²) = 2.33 km/s/Mpc
- Tension: 1.32 / 2.33 = 0.57σ

**File Creation Date:** 2025-11-14 (this work, compiled from sources above)

---

## Reproducibility Notes

### Figure Generation
All manuscript figures can be regenerated using:
```bash
python3 analysis/run_all.py
```

Individual figures:
```bash
python3 analysis/create_figure1_tension_evolution.py      # Tension waterfall
python3 analysis/create_figure2_error_budget.py           # Systematic budget
python3 analysis/create_figure3_cchp_crossval_real.py     # CCHP comparison
python3 analysis/create_figure4_h0_compilation.py         # H₀ forest plot
python3 analysis/create_figure5_hz_fit_intrinsic_scatter.py  # Cosmic chron. fit
python3 analysis/create_figure_correlation_heatmap.py     # Correlation matrix
```

### External Dependencies
The cosmic chronometer data file (`cosmic_chronometers_Hz.csv`) is included in `data/` for self-contained reproducibility. Figure 5 regeneration will use the local copy; external paths serve as fallback only.

### Version Control
All derived data files are tracked in git with full provenance in commit history:
```bash
git log --follow data/tension_evolution.csv
git log --follow data/correlation_matrix_updated.csv
```

### Data Integrity Verification
```bash
python3 analysis/run_all.py --verify
```

---

## Contact and Issues

For questions about data provenance or to report data integrity issues:
- GitHub Issues: https://github.com/ylecoyote/distance-ladder-systematics/issues
- Primary Contact: awiley@outlook.com

**Data Availability Statement:**
All derived data files and analysis scripts are publicly available in this repository. External datasets are cited with DOIs/ADS bibcodes for independent verification.

---

## Change Log

### 2025-11-18 (v8.6H - Polishing)
- **Self-contained archive**: Mirrored cosmic chronometer data to `data/cosmic_chronometers_Hz.csv`
- **Contact info**: Updated GitHub issues URL and maintainer email
- **Future updates**: Added reminder to update Freedman2025a citation when published
- Updated figure script to prioritize local data copy for reproducibility

### 2025-11-17 (v8.6H)
- Initial PROVENANCE.md creation
- Documented all external sources with citations
- Added retrieval dates and processing notes
- Expert feedback revisions branch

---

**End of Provenance Document**
