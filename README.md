# Distance Ladder Systematics and the Hubble Tension

**Forensic Analysis of Cepheid Systematic Uncertainties**

[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)
[![Journal](https://img.shields.io/badge/ApJ-Submitted-blue)](https://journals.aas.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

This repository contains the complete analysis, data, and manuscript for our investigation of systematic uncertainties in Cepheid-based Hubble constant measurements. We demonstrate that the "Hubble tension" is substantially reduced when realistic systematic error budgets are applied.

### Key Findings

- **Systematic Underestimate**: Cepheid systematic uncertainties underestimated by factor 2.4× (SH0ES 1.04 → Our 2.45 km/s/Mpc, validated by CCHP 3.10)
- **Tension Reduction**: H₀ tension reduced from 6.0σ → 1.1σ with realistic systematics
- **Multi-Method Convergence**: JAGB, cosmic chronometers, and Planck all converge at H₀ = 67.48 ± 0.50 km/s/Mpc
- **JWST Validation**: Cepheid scatter 2.3× larger than JAGB (empirical confirmation of systematic excess)

**Conclusion**: The Hubble tension is likely a measurement artifact arising from underestimated Cepheid systematics, not evidence for new physics.

---

## Repository Structure

```
distance-ladder-systematics/
├── manuscript/              # LaTeX manuscript files
│   ├── manuscript.tex       # Main manuscript (532 lines, ApJ format)
│   ├── references.bib       # Bibliography (28 references)
│   └── verify_latex.sh      # Compilation verification script
│
├── data/                    # Analysis data files
│   ├── systematic_error_budget.csv
│   ├── tension_evolution.csv
│   ├── h0_measurements_compilation.csv
│   ├── cchp_trgb_cepheid_comparison.csv
│   ├── cchp_trgb_jagb_comparison.csv
│   ├── cchp_crossval_summary.csv
│   └── tables/              # LaTeX table files (4 tables)
│
├── figures/                 # Manuscript figures
│   ├── figure1_tension_evolution.png
│   ├── figure2_error_budget_comparison.png
│   ├── figure3_cchp_crossval_real.png
│   ├── figure4_h0_compilation.png
│   └── figure5_h0_convergence.png
│
├── analysis/                # Python analysis scripts
│
├── docs/                    # Documentation
│   ├── RESEARCH_PROCESS.md  # Phases 1-4 investigation summary
│   ├── phase1_literature_review.md
│   ├── phase2_cepheid_methodology_comparison.md
│   ├── phase3_crowding_systematic_analysis.md
│   ├── phase4_metallicity_period_analysis.md
│   ├── PEER_REVIEW_RESPONSE_V*.md
│   └── LATEX_COMPILATION_GUIDE.md
│
├── README.md                # This file
├── SUBMISSION_READY.md      # Submission checklist
├── QUICK_START.md           # Fast compilation guide
├── COMPILATION_STATUS.md    # File status tracker
├── prepare_overleaf.sh      # Overleaf package creation
└── LICENSE                  # MIT License
```

---

## Quick Start

### Compile Manuscript (10 minutes)

1. **Upload to Overleaf**:
   ```bash
   ./prepare_overleaf.sh
   # Upload generated manuscript_overleaf.zip to https://www.overleaf.com
   ```

2. **Or compile locally** (requires LaTeX):
   ```bash
   cd manuscript
   pdflatex manuscript.tex
   bibtex manuscript
   pdflatex manuscript.tex
   pdflatex manuscript.tex
   ```

3. **See detailed instructions**: [QUICK_START.md](QUICK_START.md)

---

## Data Sources

All data are from publicly available sources:

- **SH0ES Cepheid distances**: Riess et al. (2022, ApJ, 934, L7)
- **JWST CCHP observations**: Freedman et al. (2025, ApJ, 985, 203)
- **Planck CMB**: Planck Collaboration (2020, A&A, 641, A6)
- **Cosmic Chronometers**: Moresco et al. (2022, Living Rev. Relativ., 25, 6)
- **Gaia parallaxes**: Lindegren et al. (2021, A&A, 649, A2)

### Data Processing

All data files in `data/` are derived from published measurements. Processing scripts are provided in `analysis/` for full reproducibility.

---

## Methodology

Our investigation employed four independent validation strategies:

1. **Systematic Error Budget Reconstruction**: Line-by-line analysis of 11 systematic error sources, comparing SH0ES claims to independent literature assessments

2. **Multi-Method Cross-Validation**: Analysis of JWST NIRCam observations comparing Cepheid, TRGB, and JAGB distances for common galaxies

3. **Independent H₀ from Cosmic Chronometers**: Model-independent H₀ measurement from 32 cosmic chronometer H(z) observations

4. **Tension Evolution Analysis**: Step-by-step tracking of how realistic systematic accounting reduces reported 6σ tension to 1.1σ

Full methodology details: [docs/RESEARCH_PROCESS.md](docs/RESEARCH_PROCESS.md)

---

## Citation

If you use this work, please cite:

```bibtex
@article{Wiley2025,
  author = {Wiley, Aaron},
  title = {{Forensic Analysis of Distance Ladder Systematics:
           The Hubble Tension Reduced from 6$\sigma$ to 1$\sigma$}},
  journal = {The Astrophysical Journal},
  year = {2025},
  note = {Submitted}
}
```

ArXiv preprint: [arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX) (to be added)

---

## Manuscript Status

- ✅ **Complete**: All sections written (5,055 words total)
- ✅ **Peer Reviewed**: 3 rounds, 18 suggestions implemented, 0 technical critiques
- ✅ **Bibliography**: 28 references, all major works cited
- ✅ **Figures/Tables**: 5 figures + 4 tables complete
- ⏳ **Status**: Submitted to The Astrophysical Journal (ApJ)

See [SUBMISSION_READY.md](SUBMISSION_READY.md) for full status.

---

## License

This work is released under the MIT License. See [LICENSE](LICENSE) for details.

Data from published sources remain under their original licenses. Please cite original sources when using derived data.

---

## Author

**Aaron Wiley**
Email: awiley@outlook.com
Independent Researcher

---

## Acknowledgments

We thank:
- SH0ES team (A. Riess et al.) for public Cepheid measurements
- Chicago-Carnegie Hubble Program (W. Freedman et al.) for JWST NIRCam photometry
- Planck Collaboration, cosmic chronometer teams, and Gaia mission

Full acknowledgments in manuscript.

---

## Contributing

This is a research repository for a submitted manuscript. Issues and discussions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

**Last updated**: October 2025
**Manuscript version**: v2.0 Final
**Repository**: https://github.com/[username]/distance-ladder-systematics
