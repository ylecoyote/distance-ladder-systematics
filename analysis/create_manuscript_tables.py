#!/usr/bin/env python3
"""
Generate the LaTeX table fragments consumed by manuscript/manuscript.tex.

This script is the checked-in source for the manuscript tables in data/tables/.
It rebuilds the current Scenario A + Prior 1 baseline from the canonical CSV
products in data/.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
TABLES_DIR = DATA_DIR / "tables"

H0_PLANCK = 67.36
SIGMA_PLANCK = 0.54

SYSTEMATIC_NAME_MAP = {
    "Parallax_Zero_Point": "Parallax Zero Point",
    "Period_Distribution": "Period Distribution",
    "Metallicity_Correction": "Metallicity Correction",
    "Crowding_Direct": "Crowding Direct",
    "Photometric_Calibration": "Photometric Calibration",
    "Extinction_Reddening": "Extinction Reddening",
    "LMC_Distance": "LMC Distance",
    "NGC4258_Distance": "NGC4258 Distance",
    "SNe_Ia_Standardization": "SNe Ia Standardization",
}

TABLE1_ORDER = [
    "Parallax_Zero_Point",
    "Period_Distribution",
    "Metallicity_Correction",
    "Crowding_Direct",
    "Photometric_Calibration",
    "Extinction_Reddening",
    "LMC_Distance",
    "NGC4258_Distance",
    "SNe_Ia_Standardization",
]

TABLE3_ORDER = [
    "SH0ES Cepheid",
    "TRGB",
    "JAGB",
    "Cosmic Chronometers (H(z))",
    "Planck CMB",
]

TABLE5_COLUMNS = [
    ("Galaxy", "Galaxy"),
    ("mu_TRGB_CCHP", "mu_trgb"),
    ("sigma_TRGB", "sigma_trgb"),
    ("mu_Cepheid_R22", "mu_cepheid"),
    ("sigma_Cepheid", "sigma_cepheid"),
    ("Delta_mu", "delta_mu"),
]


def write_table(filename: str, content: str) -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    (TABLES_DIR / filename).write_text(content, encoding="utf-8")


def quadrature(values: np.ndarray) -> float:
    return float(np.sqrt(np.sum(values**2)))


def inverse_variance_mean(values: np.ndarray, sigmas: np.ndarray) -> tuple[float, float]:
    weights = 1.0 / sigmas**2
    mean = float(np.sum(values * weights) / np.sum(weights))
    sigma = float(np.sqrt(1.0 / np.sum(weights)))
    return mean, sigma


def reduced_chi2(values: np.ndarray, sigmas: np.ndarray) -> float:
    mean, _ = inverse_variance_mean(values, sigmas)
    chi2 = float(np.sum(((values - mean) / sigmas) ** 2))
    dof = max(len(values) - 1, 1)
    return chi2 / dof


def format_ratio(shoes: float, ours: float) -> str:
    if shoes == 0:
        return r"$\infty$"
    return f"{ours / shoes:.1f}$\\times$"


def format_signed(value: float, decimals: int = 3) -> str:
    return f"{value:+.{decimals}f}"


def format_galaxy(name: str) -> str:
    if name.startswith("NGC") and len(name) > 3 and name[3:].isdigit():
        return f"NGC {name[3:]}"
    return name


def build_table1() -> None:
    budget = pd.read_csv(DATA_DIR / "systematic_error_budget.csv", comment="#")
    corr = pd.read_csv(DATA_DIR / "correlation_matrix_updated.csv", index_col=0, comment="#")

    filtered = budget[budget["Error_Source"].isin(TABLE1_ORDER)].copy()
    filtered["Display_Name"] = filtered["Error_Source"].map(SYSTEMATIC_NAME_MAP)
    filtered["Sort_Key"] = filtered["Error_Source"].map({name: i for i, name in enumerate(TABLE1_ORDER)})
    filtered = filtered.sort_values("Sort_Key")

    shoes = filtered["SH0ES_Estimate_km_s_Mpc"].to_numpy(dtype=float)
    ours = filtered["Our_Assessment_km_s_Mpc"].to_numpy(dtype=float)
    corr_matrix = corr.to_numpy(dtype=float)

    shoes_uncorr = quadrature(shoes)
    ours_uncorr = quadrature(ours)
    shoes_corr = float(np.sqrt(shoes.T @ corr_matrix @ shoes))
    ours_corr = float(np.sqrt(ours.T @ corr_matrix @ ours))

    rows = []
    for _, row in filtered.iterrows():
        rows.append(
            f"{row['Display_Name']} & "
            f"{row['SH0ES_Estimate_km_s_Mpc']:.1f} & "
            f"{row['Our_Assessment_km_s_Mpc']:.1f} & "
            f"{format_ratio(float(row['SH0ES_Estimate_km_s_Mpc']), float(row['Our_Assessment_km_s_Mpc']))} & "
            f"{row['Confidence_Level']} \\\\"
        )

    content = "\n".join(
        [
            "% Table 1: Systematic Error Budget for Cepheid-based H0 Measurements",
            "% Generated from systematic_error_budget.csv and correlation_matrix_updated.csv",
            "% Scenario A + Prior 1 baseline",
            "",
            r"\begin{deluxetable*}{lcccc}",
            r"\tablecaption{Systematic Error Budget for Cepheid-based H$_0$ Measurements\label{tab:systematic_budget}}",
            r"\tablewidth{0pt}",
            r"\tablehead{",
            r"\colhead{Error Source} &",
            r"\colhead{SH0ES} &",
            r"\colhead{Our Assessment} &",
            r"\colhead{Ratio} &",
            r"\colhead{Confidence} \\",
            r"\colhead{} &",
            r"\colhead{(km~s$^{-1}$~Mpc$^{-1}$)} &",
            r"\colhead{(km~s$^{-1}$~Mpc$^{-1}$)} &",
            r"\colhead{(Ours/SH0ES)} &",
            r"\colhead{Level}",
            r"}",
            r"\startdata",
            *rows,
            r"\hline",
            f"Total (uncorrelated) & {shoes_uncorr:.2f} & {ours_uncorr:.2f} & {(ours_uncorr / shoes_uncorr):.1f}$\\times$ & --- \\\\",
            f"Total (correlated) & {shoes_corr:.2f} & {ours_corr:.2f} & {(ours_corr / shoes_corr):.1f}$\\times$ & --- \\\\",
            r"\enddata",
            (
                r"\tablecomments{Systematic uncertainty budget for 9 independent sources (Scenario A + Prior 1 baseline). "
                r"Values are rebuilt from the machine-readable CSV products in this repository. "
                r"SH0ES values correspond to the quoted component-level budget; our reassessment adopts the 2025 consensus baseline "
                r"$\gamma=-0.2\pm0.1$ for metallicity and removes covariant crowding as a standalone term while retaining its "
                r"effect through the correlation matrix. "
                rf"Quadrature sums give $\sigma_{{\rm sys,uncorr}} = {ours_uncorr:.2f}$ km~s$^{{-1}}$~Mpc$^{{-1}}$; "
                rf"full covariance propagation gives $\sigma_{{\rm sys,corr}} = {ours_corr:.2f}$ km~s$^{{-1}}$~Mpc$^{{-1}}$, "
                rf"an {(ours_corr / ours_uncorr - 1.0) * 100:.0f}\% increase over the independence assumption. "
                r"CCHP \citep{Freedman2025a} JWST cross-validation provides independent observational support for the enlarged Cepheid "
                r"budget through the factor 2.3 excess Cepheid scatter summarized in Table~\ref{tab:cchp_crossval}.}"
            ),
            r"\end{deluxetable*}",
            "",
        ]
    )

    write_table("table1_systematic_budget.tex", content)


def build_table2() -> None:
    df = pd.read_csv(DATA_DIR / "tension_evolution.csv", comment="#")
    tensions = df["Tension_sigma"].to_numpy(dtype=float)

    stage_labels = [
        "Stat. only",
        "Quoted SH0ES sys. + stat.",
        "After parallax (Scenario A)",
        "After period",
        "+ Metallicity + correlated sys.",
    ]

    rows = []
    for idx, (_, row) in enumerate(df.iterrows(), start=1):
        rows.append(
            f"{idx} & "
            f"{row['H0_km_s_Mpc']:.2f} & "
            f"{row['Sigma_km_s_Mpc']:.2f} & "
            f"{row['Tension_sigma']:.1f}$\\sigma$ & "
            f"{stage_labels[idx - 1]} \\\\"
        )

    reduction_factor = tensions[0] / tensions[-1]

    content = "\n".join(
        [
            "% Table 2: H0 Tension Evolution Through Five Stages",
            "% Generated from tension_evolution.csv",
            "% Scenario A + Prior 1 baseline",
            "",
            r"\begin{deluxetable*}{lcccc}",
            r"\tablecaption{H$_0$ Tension Evolution Through Five Stages\label{tab:tension_stages}}",
            r"\tablewidth{0pt}",
            r"\tablehead{",
            r"\colhead{Stage} &",
            r"\colhead{H$_0$} &",
            r"\colhead{$\sigma_{\rm total}$} &",
            r"\colhead{Tension} &",
            r"\colhead{Description} \\",
            r"\colhead{} &",
            r"\colhead{(km~s$^{-1}$~Mpc$^{-1}$)} &",
            r"\colhead{(km~s$^{-1}$~Mpc$^{-1}$)} &",
            r"\colhead{(vs Planck)} &",
            r"\colhead{}",
            r"}",
            r"\startdata",
            *rows,
            r"\enddata",
            (
                r"\tablecomments{Progressive reduction of Hubble tension through realistic systematic accounting "
                r"(Scenario A + Prior 1 baseline). Stage 1 uses the statistical uncertainty only. "
                r"Stage 2 reconstructs the SH0ES ladder using the quoted component budget: "
                r"$\sigma_{\rm total} = \sqrt{0.80^2 + 1.04^2} = 1.31$ km~s$^{-1}$~Mpc$^{-1}$. "
                r"Stage 3 applies Scenario A parallax handling with no additional H$_0$ shift. "
                r"Stage 4 applies the period-distribution correction of $-2.5$ km~s$^{-1}$~Mpc$^{-1}$ and adds the "
                r"$\pm 1.0$ km~s$^{-1}$~Mpc$^{-1}$ period uncertainty in quadrature, giving "
                r"$\sigma_{\rm total} = 1.65$ km~s$^{-1}$~Mpc$^{-1}$ and a 1.8$\sigma$ Planck-relative tension. "
                r"Stage 5 applies the metallicity correction ($-1.0$ km~s$^{-1}$~Mpc$^{-1}$) and the realistic correlated "
                r"systematic budget $\sigma_{\rm sys,corr} = 1.71$ km~s$^{-1}$~Mpc$^{-1}$, giving "
                r"$\sigma_{\rm total} = \sqrt{0.80^2 + 1.71^2} = 1.89$ km~s$^{-1}$~Mpc$^{-1}$. "
                rf"The baseline tension is reduced from {tensions[0]:.1f}$\sigma$ to {tensions[-1]:.1f}$\sigma$ "
                rf"({reduction_factor:.1f}$\times$)."
                r"}"
            ),
            r"\end{deluxetable*}",
            "",
        ]
    )

    write_table("table2_tension_evolution.tex", content)


def build_table3() -> None:
    df = pd.read_csv(DATA_DIR / "h0_measurements_compilation.csv", comment="#")

    main_rows = []
    for method in TABLE3_ORDER:
        row = df.loc[df["Method"] == method].iloc[0]
        main_rows.append(
            f"{method} & {row['H0_km_s_Mpc']:.2f} & {row['Sigma_km_s_Mpc']:.2f} & "
            + (
                r"\citet{Riess2022} \\"
                if method == "SH0ES Cepheid"
                else r"\citet{Freedman2025a} \\"
                if method in {"TRGB", "JAGB"}
                else r"\citet{Planck2018} \\"
                if method == "Planck CMB"
                else r"This work \\"
            )
        )

    jagb = df.loc[df["Method"] == "JAGB"].iloc[0]
    cc = df.loc[df["Method"] == "Cosmic Chronometers (H(z))"].iloc[0]
    planck = df.loc[df["Method"] == "Planck CMB"].iloc[0]
    jagb_cc = df.loc[df["Method"] == "JAGB + Cosmic Chron."].iloc[0]
    weighted = df.loc[df["Method"] == "Weighted Mean"].iloc[0]
    corrected = df.loc[df["Method"] == "Corrected Cepheid (Scenario A + Prior 1)"].iloc[0]

    chi2_jagb_cc = reduced_chi2(
        np.array([jagb["H0_km_s_Mpc"], cc["H0_km_s_Mpc"]], dtype=float),
        np.array([jagb["Sigma_km_s_Mpc"], cc["Sigma_km_s_Mpc"]], dtype=float),
    )
    chi2_three = reduced_chi2(
        np.array([jagb["H0_km_s_Mpc"], cc["H0_km_s_Mpc"], planck["H0_km_s_Mpc"]], dtype=float),
        np.array([jagb["Sigma_km_s_Mpc"], cc["Sigma_km_s_Mpc"], planck["Sigma_km_s_Mpc"]], dtype=float),
    )
    corrected_vs_planck_free = abs(corrected["H0_km_s_Mpc"] - jagb_cc["H0_km_s_Mpc"]) / np.sqrt(
        corrected["Sigma_km_s_Mpc"] ** 2 + jagb_cc["Sigma_km_s_Mpc"] ** 2
    )

    content = "\n".join(
        [
            "% Table 3: H0 Measurement Compilation and Multi-Method Convergence",
            "% Generated from h0_measurements_compilation.csv",
            "",
            r"\begin{deluxetable*}{lccc}",
            r"\tablecaption{H$_0$ Measurement Compilation and Multi-Method Convergence\label{tab:h0_compilation}}",
            r"\tablewidth{0pt}",
            r"\tablehead{",
            r"\colhead{Method} &",
            r"\colhead{H$_0$} &",
            r"\colhead{$\sigma$} &",
            r"\colhead{Reference} \\",
            r"\colhead{} &",
            r"\colhead{(km~s$^{-1}$~Mpc$^{-1}$)} &",
            r"\colhead{(km~s$^{-1}$~Mpc$^{-1}$)} &",
            r"\colhead{}",
            r"}",
            r"\startdata",
            *main_rows,
            r"\hline",
            r"\multicolumn{4}{c}{\textit{Late-Universe (Planck-Independent)}} \\",
            r"\hline",
            f"JAGB + Cosmic Chron. & {jagb_cc['H0_km_s_Mpc']:.2f} & {jagb_cc['Sigma_km_s_Mpc']:.2f} & This work \\\\",
            r"\hline",
            r"\multicolumn{4}{c}{\textit{Three-Method Convergence (incl. Planck)}} \\",
            r"\hline",
            f"Weighted Mean & {weighted['H0_km_s_Mpc']:.2f} & {weighted['Sigma_km_s_Mpc']:.2f} & This work \\\\",
            r"\enddata",
            (
                r"\tablecomments{Compilation of H\ensuremath{_0} measurements from different methods revealing systematic gradient and convergence. "
                rf"SH0ES Cepheid is shown with the published Riess et al.\ (2022) uncertainty "
                rf"({df.loc[df['Method'] == 'SH0ES Cepheid', 'Sigma_km_s_Mpc'].iloc[0]:.2f}\,km\,s\ensuremath{{^{{-1}}}}\,Mpc\ensuremath{{^{{-1}}}}). "
                rf"Corrected Cepheid (baseline Scenario A + Prior 1, not shown in the main rows) is "
                rf"\ensuremath{{H_0 = {corrected['H0_km_s_Mpc']:.2f} \pm {corrected['Sigma_km_s_Mpc']:.2f}}}\,km\,s\ensuremath{{^{{-1}}}}\,Mpc\ensuremath{{^{{-1}}}} after applying realistic "
                r"correlated systematics and the period and metallicity bias corrections. "
                rf"JAGB + cosmic chronometers give a Planck-independent mean of \ensuremath{{{jagb_cc['H0_km_s_Mpc']:.2f} \pm {jagb_cc['Sigma_km_s_Mpc']:.2f}}}\,"
                rf"km\,s\ensuremath{{^{{-1}}}}\,Mpc\ensuremath{{^{{-1}}}} with \ensuremath{{\chi^2_{{\rm red}} \approx {chi2_jagb_cc:.2f}}}; "
                rf"the corrected Cepheid value differs from this Planck-free mean by \ensuremath{{{corrected_vs_planck_free:.1f}\sigma}}. "
                rf"The three-method weighted mean of JAGB, cosmic chronometers, and Planck is "
                rf"\ensuremath{{{weighted['H0_km_s_Mpc']:.2f} \pm {weighted['Sigma_km_s_Mpc']:.2f}}}\,km\,s\ensuremath{{^{{-1}}}}\,Mpc\ensuremath{{^{{-1}}}} with "
                rf"\ensuremath{{\chi^2_{{\rm red}} = {chi2_three:.2f}}}, showing strong cross-method convergence."
                r"}"
            ),
            r"\end{deluxetable*}",
            "",
        ]
    )

    write_table("table3_h0_compilation.tex", content)


def build_table4() -> None:
    summary = pd.read_csv(DATA_DIR / "cchp_crossval_summary.csv")
    jagb_row = summary.loc[summary["Comparison"] == "JAGB vs TRGB"].iloc[0]
    cepheid_row = summary.loc[summary["Comparison"] == "Cepheid vs TRGB"].iloc[0]
    scatter_ratio = cepheid_row["RMS_Scatter_mag"] / jagb_row["RMS_Scatter_mag"]

    content = "\n".join(
        [
            "% Table 4: JWST NIRCam Multi-Method Cross-Validation Summary",
            "% Generated from cchp_crossval_summary.csv",
            "",
            r"\begin{deluxetable*}{lcccc}",
            r"\tablecaption{\textit{JWST} NIRCam Multi-Method Cross-Validation Summary\label{tab:cchp_crossval}}",
            r"\tablewidth{0pt}",
            r"\tablehead{",
            r"\colhead{Comparison} &",
            r"\colhead{N} &",
            r"\colhead{$\langle\Delta\mu\rangle$} &",
            r"\colhead{RMS} &",
            r"\colhead{Interpretation} \\",
            r"\colhead{} &",
            r"\colhead{(galaxies)} &",
            r"\colhead{(mag)} &",
            r"\colhead{(mag)} &",
            r"\colhead{}",
            r"}",
            r"\startdata",
            f"JAGB vs TRGB & {int(jagb_row['N_galaxies'])} & {format_signed(float(jagb_row['Weighted_Mean_Δμ_mag']), 4)} & {jagb_row['RMS_Scatter_mag']:.3f} & $<$1\\% distance agreement \\\\",
            f"Cepheid vs TRGB & {int(cepheid_row['N_galaxies'])} & {format_signed(float(cepheid_row['Weighted_Mean_Δμ_mag']), 4)} & {cepheid_row['RMS_Scatter_mag']:.3f} & {scatter_ratio:.1f}$\\times$ excess scatter \\\\",
            r"\hline",
            f"\\multicolumn{{5}}{{c}}{{Scatter Ratio: Cepheid/JAGB = {scatter_ratio:.1f}$\\times$}} \\\\",
            r"\enddata",
            (
                r"\tablecomments{Summary of CCHP \textit{JWST} NIRCam distance-modulus comparisons \citep{Freedman2025a}. "
                rf"JAGB vs TRGB shows a weighted mean offset of {format_signed(float(jagb_row['Weighted_Mean_Δμ_mag']), 4)} mag "
                rf"with RMS scatter {jagb_row['RMS_Scatter_mag']:.3f} mag, establishing the JWST precision baseline for stellar-population indicators. "
                rf"Cepheid vs TRGB shows a weighted mean offset of {format_signed(float(cepheid_row['Weighted_Mean_Δμ_mag']), 4)} mag "
                rf"with RMS scatter {cepheid_row['RMS_Scatter_mag']:.3f} mag, a factor {scatter_ratio:.1f} larger than the JAGB--TRGB baseline. "
                r"This provides direct observational support for enlarged Cepheid systematic uncertainties.}"
            ),
            r"\end{deluxetable*}",
            "",
        ]
    )

    write_table("table4_cchp_crossval.tex", content)


def build_table5() -> None:
    df = pd.read_csv(DATA_DIR / "cchp_trgb_cepheid_comparison.csv", comment="#")
    rows = []
    for _, row in df.iterrows():
        rows.append(
            f"{format_galaxy(row['Galaxy'])} & "
            f"{row['mu_TRGB_CCHP']:.3f} & {row['sigma_TRGB']:.3f} & "
            f"{row['mu_Cepheid_R22']:.3f} & {row['sigma_Cepheid']:.3f} & "
            f"${format_signed(float(row['Delta_mu']), 3)}$ \\\\"
        )

    weights = 1.0 / df["Delta_sigma"].to_numpy(dtype=float) ** 2
    weighted_mean = float(np.sum(df["Delta_mu"] * weights) / np.sum(weights))
    weighted_sigma = float(np.sqrt(1.0 / np.sum(weights)))
    rms = float(np.sqrt(np.mean(df["Delta_mu"].to_numpy(dtype=float) ** 2)))

    content = "\n".join(
        [
            "% Table 5: Per-Galaxy JWST Cross-Validation (TRGB vs Cepheid)",
            "% Generated from cchp_trgb_cepheid_comparison.csv",
            "",
            r"\begin{deluxetable*}{lccccc}",
            r"\tablecaption{Per-Galaxy JWST NIRCam Cross-Validation: TRGB vs Cepheid Distance Moduli\label{tab:jwst_galaxies}}",
            r"\tablewidth{0pt}",
            r"\tablehead{",
            r"\colhead{Galaxy} &",
            r"\colhead{$\mu_{\rm TRGB}$} &",
            r"\colhead{$\sigma_{\rm TRGB}$} &",
            r"\colhead{$\mu_{\rm Cepheid}$} &",
            r"\colhead{$\sigma_{\rm Cepheid}$} &",
            r"\colhead{$\Delta\mu$} \\",
            r"\colhead{} &",
            r"\colhead{(mag)} &",
            r"\colhead{(mag)} &",
            r"\colhead{(mag)} &",
            r"\colhead{(mag)} &",
            r"\colhead{(mag)}",
            r"}",
            r"\startdata",
            *rows,
            r"\enddata",
            (
                r"\tablenotetext{}{TRGB distance moduli are from CCHP \textit{JWST} NIRCam observations \citep{Freedman2025a}; "
                r"Cepheid distance moduli are from SH0ES \citep{Riess2022}. "
                rf"The weighted mean offset is $\langle\Delta\mu\rangle = {weighted_mean:+.3f} \pm {weighted_sigma:.3f}$ mag, "
                rf"with RMS scatter {rms:.3f} mag. "
                r"Offset $\Delta\mu = \mu_{\rm Cepheid} - \mu_{\rm TRGB}$.}"
            ),
            r"\end{deluxetable*}",
            "",
        ]
    )

    write_table("table5_jwst_crossvalidation.tex", content)


def build_table6() -> None:
    df = pd.read_csv(DATA_DIR / "cosmic_chronometers_Hz.csv", comment="#")
    rows = []
    for _, row in df.iterrows():
        reference = str(row["reference"]).replace("_", r"\_")
        rows.append(
            f"{row['z']:.3f} & {row['Hz']:.1f} & {row['sigma_Hz']:.1f} & {reference} \\\\"
        )

    cc_row = pd.read_csv(DATA_DIR / "h0_measurements_compilation.csv", comment="#")
    cc_row = cc_row.loc[cc_row["Method"] == "Cosmic Chronometers (H(z))"].iloc[0]

    content = "\n".join(
        [
            "% Table 6: Cosmic Chronometer H(z) Measurements",
            "% Generated from cosmic_chronometers_Hz.csv",
            "",
            r"\begin{deluxetable*}{cccc}",
            r"\tablecaption{Cosmic Chronometer H(z) Measurements\label{tab:cosmic_chronometers}}",
            r"\tablewidth{0pt}",
            r"\tablehead{",
            r"\colhead{Redshift} &",
            r"\colhead{H(z)} &",
            r"\colhead{$\sigma_{H(z)}$} &",
            r"\colhead{Reference} \\",
            r"\colhead{$z$} &",
            r"\colhead{(km~s$^{-1}$~Mpc$^{-1}$)} &",
            r"\colhead{(km~s$^{-1}$~Mpc$^{-1}$)} &",
            r"\colhead{}",
            r"}",
            r"\startdata",
            *rows,
            r"\enddata",
            (
                r"\tablecomments{Compilation of 32 cosmic chronometer H(z) measurements used in this work. "
                r"These data provide a distance-ladder-independent constraint on the expansion history from differential galaxy ages. "
                rf"Fitting flat $\Lambda$CDM with fixed $\Omega_m = 0.315$ gives "
                rf"H$_0 = {cc_row['H0_km_s_Mpc']:.2f} \pm {cc_row['Sigma_km_s_Mpc']:.2f}$ km~s$^{{-1}}$~Mpc$^{{-1}}$."
                r"}"
            ),
            r"\end{deluxetable*}",
            "",
        ]
    )

    write_table("table6_cosmic_chronometers.tex", content)


def build_anchor_weights() -> None:
    content = "\n".join(
        [
            "% Table: Anchor Distance Calibrators and Weighting",
            "% Static manuscript support table",
            "",
            r"\begin{deluxetable*}{lcccccc}",
            r"\tablecaption{Cepheid Distance Anchor Calibrators and H$_0$ Weighting\label{tab:anchor_weights}}",
            r"\tablewidth{0pt}",
            r"\tablehead{",
            r"\colhead{Anchor} &",
            r"\colhead{Distance} &",
            r"\colhead{Method} &",
            r"\colhead{$\bar{\varpi}$} &",
            r"\colhead{$\Delta\varpi$} &",
            r"\colhead{Weight} &",
            r"\colhead{$\Delta H_0$} \\",
            r"\colhead{} &",
            r"\colhead{(Mpc)} &",
            r"\colhead{} &",
            r"\colhead{(mas)} &",
            r"\colhead{(mas)} &",
            r"\colhead{(\%)} &",
            r"\colhead{(km~s$^{-1}$~Mpc$^{-1}$)}",
            r"}",
            r"\startdata",
            r"Milky Way Cepheids & 0.7--2.0 & Gaia parallax & 0.70 & +0.017 & 60 & +1.8 \\",
            r"LMC & 0.050 & Geometric (DEBs) & --- & 0.000 & 25 & 0.0 \\",
            r"NGC 4258 & 7.6 & Maser (H$_2$O) & --- & 0.000 & 15 & 0.0 \\",
            r"\hline",
            r"\multicolumn{6}{l}{Effective diluted bias:} & +1.1 \\",
            r"\multicolumn{6}{l}{Adopted correction:} & $-1.0$ \\",
            r"\enddata",
            (
                r"\tablecomments{Distance anchor calibrators used in SH0ES Cepheid-based H$_0$ measurements. "
                r"The approximate weighting is retained here as a manuscript support table for the parallax-dilution argument in the text.}"
            ),
            r"\end{deluxetable*}",
            "",
        ]
    )

    write_table("table_anchor_weights.tex", content)


def build_correlation_matrix_table() -> None:
    corr = pd.read_csv(DATA_DIR / "correlation_matrix_updated.csv", index_col=0, comment="#")
    short_names = [
        "Parallax ZP",
        "Period Dist.",
        "Metallicity",
        "Crowding Direct",
        "Photometry",
        "Extinction",
        "LMC Distance",
        "NGC4258 Distance",
        "SNe Ia Std.",
    ]

    rows = []
    for idx, (row_name, values) in enumerate(corr.iterrows(), start=1):
        short_name = short_names[idx - 1]
        value_str = " & ".join(f"{float(v):.2f}" for v in values.to_numpy(dtype=float))
        rows.append(f"({idx}) {short_name} & {value_str} \\\\")

    content = "\n".join(
        [
            "% Table: 9x9 Correlation Matrix for Systematic Error Budget",
            "% Generated from correlation_matrix_updated.csv",
            "",
            r"\begin{deluxetable*}{lccccccccc}",
            r"\tablecaption{Correlation Matrix for Systematic Error Sources \label{tab:correlation_matrix}}",
            r"\tablewidth{0pt}",
            r"\tablehead{",
            r"\colhead{Error Source} &",
            r"\colhead{(1)} &",
            r"\colhead{(2)} &",
            r"\colhead{(3)} &",
            r"\colhead{(4)} &",
            r"\colhead{(5)} &",
            r"\colhead{(6)} &",
            r"\colhead{(7)} &",
            r"\colhead{(8)} &",
            r"\colhead{(9)}",
            r"}",
            r"\startdata",
            *rows,
            r"\enddata",
            (
                r"\tablecomments{Correlation matrix $\mathbf{R}$ (9$\times$9) used for covariance propagation in the systematic budget. "
                r"Matrix entries are regenerated directly from data/correlation\_matrix\_updated.csv. "
                r"Positive off-diagonal terms encode physically motivated correlations among period, metallicity, crowding, extinction, "
                r"photometric calibration, and SNe Ia standardization.}"
            ),
            r"\end{deluxetable*}",
            "",
        ]
    )

    write_table("table_correlation_matrix.tex", content)


def main() -> None:
    build_table1()
    build_table2()
    build_table3()
    build_table4()
    build_table5()
    build_table6()
    build_anchor_weights()
    build_correlation_matrix_table()

    print(f"Generated manuscript tables in {TABLES_DIR}")


if __name__ == "__main__":
    main()
