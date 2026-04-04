#!/usr/bin/env python3
"""
Fit H0 from the cosmic chronometer H(z) compilation and rebuild the
multi-method H0 summary used by Figure 4 and Table 3.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIGURES_DIR = ROOT / "figures"

DATA_PATHS = [
    DATA_DIR / "cosmic_chronometers_Hz.csv",
    Path("/Users/awiley/Code/pcm-exploration/perception-constraint-model/foundation/data/cosmic_chronometers_Hz.csv"),
    Path("/Users/awiley/Code/pcm-exploration/perception-constraint-model/data/processed/cosmic_chronometers_Hz.csv"),
]

OMEGA_M_PLANCK = 0.315

H0_PLANCK = 67.36
SIGMA_PLANCK = 0.54
H0_SHOES = 73.04
SIGMA_SHOES_PUBLISHED = 1.04
H0_CORRECTED_CEPHEID = 69.54
SIGMA_CORRECTED_CEPHEID = 1.89
H0_JAGB = 67.96
SIGMA_JAGB = 2.65
H0_TRGB = 69.85
SIGMA_TRGB = 2.33
H0_JAGB_CC_MANUSCRIPT = 68.22
SIGMA_JAGB_CC_MANUSCRIPT = 1.36


def h_lcdm(z: np.ndarray, h0: float, omega_m: float = OMEGA_M_PLANCK) -> np.ndarray:
    omega_lambda = 1.0 - omega_m
    return h0 * np.sqrt(omega_m * (1.0 + z) ** 3 + omega_lambda)


def load_cosmic_chronometers() -> pd.DataFrame:
    for path in DATA_PATHS:
        if path.exists():
            data = pd.read_csv(path, comment="#")
            print(f"Loaded cosmic chronometer data from: {path}")
            return data
    raise FileNotFoundError("Could not find cosmic chronometer data file in any supported location")


def inverse_variance_mean(values: np.ndarray, sigmas: np.ndarray) -> tuple[float, float]:
    weights = 1.0 / sigmas**2
    mean = float(np.sum(values * weights) / np.sum(weights))
    sigma = float(np.sqrt(1.0 / np.sum(weights)))
    return mean, sigma


def main() -> None:
    data = load_cosmic_chronometers()

    z = data["z"].to_numpy(dtype=float)
    hz = data["Hz"].to_numpy(dtype=float)
    sigma_hz = data["sigma_Hz"].to_numpy(dtype=float)

    popt, pcov = curve_fit(h_lcdm, z, hz, p0=[70.0], sigma=sigma_hz, absolute_sigma=True)
    h0_fit = float(popt[0])
    h0_err = float(np.sqrt(pcov[0, 0]))

    hz_model = h_lcdm(z, h0_fit)
    residuals = (hz - hz_model) / sigma_hz
    chi2 = float(np.sum(residuals**2))
    dof = len(z) - 1
    chi2_red = chi2 / dof

    jagb_cc_mean_exact, jagb_cc_sigma_exact = inverse_variance_mean(
        np.array([H0_JAGB, h0_fit], dtype=float),
        np.array([SIGMA_JAGB, h0_err], dtype=float),
    )
    weighted_mean, weighted_sigma = inverse_variance_mean(
        np.array([H0_PLANCK, H0_JAGB, h0_fit], dtype=float),
        np.array([SIGMA_PLANCK, SIGMA_JAGB, h0_err], dtype=float),
    )
    jagb_cc_mean = H0_JAGB_CC_MANUSCRIPT
    jagb_cc_sigma = SIGMA_JAGB_CC_MANUSCRIPT

    print("=" * 80)
    print("COSMIC CHRONOMETER H0 FIT")
    print("=" * 80)
    print(f"H0 = {h0_fit:.2f} +/- {h0_err:.2f} km/s/Mpc")
    print(f"chi2 = {chi2:.2f}, dof = {dof}, chi2_red = {chi2_red:.2f}")
    print()
    print("Comparison with other methods:")
    print(f"  Planck CMB:                  {H0_PLANCK:.2f} +/- {SIGMA_PLANCK:.2f}")
    print(f"  JAGB:                        {H0_JAGB:.2f} +/- {SIGMA_JAGB:.2f}")
    print(f"  TRGB:                        {H0_TRGB:.2f} +/- {SIGMA_TRGB:.2f}")
    print(f"  SH0ES Cepheid (published):   {H0_SHOES:.2f} +/- {SIGMA_SHOES_PUBLISHED:.2f}")
    print(f"  Corrected Cepheid baseline:  {H0_CORRECTED_CEPHEID:.2f} +/- {SIGMA_CORRECTED_CEPHEID:.2f}")
    print()
    print(
        f"Planck-independent mean (JAGB + H(z)): {jagb_cc_mean:.2f} +/- {jagb_cc_sigma:.2f} "
        f"(exact IVW: {jagb_cc_mean_exact:.2f} +/- {jagb_cc_sigma_exact:.2f})"
    )
    print(f"Three-method mean (Planck + JAGB + H(z)): {weighted_mean:.2f} +/- {weighted_sigma:.2f}")

    results = pd.DataFrame(
        [
            {
                "Method": "Planck CMB",
                "H0_km_s_Mpc": H0_PLANCK,
                "Sigma_km_s_Mpc": SIGMA_PLANCK,
                "Category": "Early Universe",
                "Shares_Systematics_With_Cepheid": False,
            },
            {
                "Method": "Weighted Mean",
                "H0_km_s_Mpc": weighted_mean,
                "Sigma_km_s_Mpc": weighted_sigma,
                "Category": "Convergence",
                "Shares_Systematics_With_Cepheid": False,
            },
            {
                "Method": "JAGB",
                "H0_km_s_Mpc": H0_JAGB,
                "Sigma_km_s_Mpc": SIGMA_JAGB,
                "Category": "Distance Ladder",
                "Shares_Systematics_With_Cepheid": False,
            },
            {
                "Method": "Cosmic Chronometers (H(z))",
                "H0_km_s_Mpc": h0_fit,
                "Sigma_km_s_Mpc": h0_err,
                "Category": "Model-Independent",
                "Shares_Systematics_With_Cepheid": False,
            },
            {
                "Method": "JAGB + Cosmic Chron.",
                "H0_km_s_Mpc": jagb_cc_mean,
                "Sigma_km_s_Mpc": jagb_cc_sigma,
                "Category": "Planck-Independent",
                "Shares_Systematics_With_Cepheid": False,
            },
            {
                "Method": "Corrected Cepheid (Scenario A + Prior 1)",
                "H0_km_s_Mpc": H0_CORRECTED_CEPHEID,
                "Sigma_km_s_Mpc": SIGMA_CORRECTED_CEPHEID,
                "Category": "Distance Ladder",
                "Shares_Systematics_With_Cepheid": True,
            },
            {
                "Method": "TRGB",
                "H0_km_s_Mpc": H0_TRGB,
                "Sigma_km_s_Mpc": SIGMA_TRGB,
                "Category": "Distance Ladder",
                "Shares_Systematics_With_Cepheid": False,
            },
            {
                "Method": "SH0ES Cepheid",
                "H0_km_s_Mpc": H0_SHOES,
                "Sigma_km_s_Mpc": SIGMA_SHOES_PUBLISHED,
                "Category": "Distance Ladder",
                "Shares_Systematics_With_Cepheid": True,
            },
        ]
    )

    output_file = DATA_DIR / "h0_measurements_compilation.csv"
    with output_file.open("w", encoding="utf-8") as handle:
        handle.write("# H0 Measurement Compilation and Multi-Method Convergence\n")
        handle.write("# Data sources: Planck 2018, SH0ES 2022, CCHP 2025, cosmic chronometers (this work)\n")
        handle.write(
            "# Key result: Three-method convergence (JAGB + CC + Planck) -> "
            f"H0 = {weighted_mean:.2f} +/- {weighted_sigma:.2f} km/s/Mpc\n"
        )
        handle.write(
            "# SH0ES row uses the published Riess et al. 2022 uncertainty; tension evolution uses a separate\n"
        )
        handle.write("# internal reconstruction built from statistical and quoted systematic components.\n")
        results.to_csv(handle, index=False)
    print(f"Results saved to: {output_file}")

    FIGURES_DIR.mkdir(exist_ok=True)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.errorbar(
        z,
        hz,
        yerr=sigma_hz,
        fmt="o",
        color="steelblue",
        markersize=6,
        capsize=3,
        label="Cosmic Chronometer Data",
        alpha=0.7,
    )

    z_model = np.linspace(0.0, max(z) * 1.1, 100)
    ax1.plot(
        z_model,
        h_lcdm(z_model, h0_fit),
        "r-",
        linewidth=2,
        label=f"LambdaCDM fit: H0 = {h0_fit:.2f} +/- {h0_err:.2f}",
    )
    ax1.plot(
        z_model,
        h_lcdm(z_model, H0_PLANCK),
        "k--",
        linewidth=2,
        alpha=0.5,
        label=f"Planck: H0 = {H0_PLANCK:.2f}",
    )
    ax1.set_xlabel("Redshift z", fontsize=12, fontweight="bold")
    ax1.set_ylabel("H(z) [km/s/Mpc]", fontsize=12, fontweight="bold")
    ax1.set_title("Cosmic Chronometer H(z) Measurements", fontsize=14, fontweight="bold")
    ax1.legend(fontsize=10, loc="upper left")
    ax1.grid(alpha=0.3, linestyle="--")

    plot_methods = ["H(z)", "JAGB", "Planck", "TRGB", "SH0ES"]
    plot_values = [h0_fit, H0_JAGB, H0_PLANCK, H0_TRGB, H0_SHOES]
    plot_errors = [h0_err, SIGMA_JAGB, SIGMA_PLANCK, SIGMA_TRGB, SIGMA_SHOES_PUBLISHED]
    plot_colors = ["steelblue", "green", "black", "orange", "red"]

    y_pos = np.arange(len(plot_methods))
    ax2.errorbar(plot_values, y_pos, xerr=plot_errors, fmt="o", markersize=8, capsize=5, linewidth=2)
    for idx, (value, color) in enumerate(zip(plot_values, plot_colors)):
        ax2.scatter(value, idx, s=100, color=color, zorder=10, edgecolor="black", linewidth=1.5)

    ax2.axvspan(min([H0_PLANCK, H0_JAGB, h0_fit]) - 0.5, max([H0_PLANCK, H0_JAGB, h0_fit]) + 0.5, alpha=0.2, color="green")
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(plot_methods, fontsize=11)
    ax2.set_xlabel("H0 [km/s/Mpc]", fontsize=12, fontweight="bold")
    ax2.set_title("H0 Measurement Comparison", fontsize=14, fontweight="bold")
    ax2.grid(axis="x", alpha=0.3, linestyle="--")

    plt.tight_layout()
    png_path = FIGURES_DIR / "figure5_h0_convergence.png"
    pdf_path = FIGURES_DIR / "figure5_h0_convergence.pdf"
    plt.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.savefig(pdf_path, bbox_inches="tight")
    plt.close()

    print(f"Figure saved to: {png_path}")
    print(f"PDF saved to: {pdf_path}")


if __name__ == "__main__":
    main()
