#!/usr/bin/env python3
"""
Generate Figure 1: Tension Evolution Visualization
Shows progressive reduction of Hubble tension through 5 stages + conservative scenario

Data source: data/tension_evolution.csv
Output: figures/figure1_tension_evolution.png (publication quality)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Planck 2018 values
PLANCK_H0 = 67.36
PLANCK_SIGMA = 0.54

def create_tension_evolution_figure():
    """Create publication-quality tension evolution figure"""

    # Load data
    data = pd.read_csv('data/tension_evolution.csv')

    # Add Stage 5B (Conservative scenario) from Table 2
    conservative_row = pd.DataFrame([{
        'Stage': 'Conservative (no corrections)',
        'H0_km_s_Mpc': 73.17,
        'Sigma_km_s_Mpc': 2.58,
        'Tension_sigma': 2.2,
        'Description': 'Conservative scenario (no bias corrections)'
    }])

    # Prepare data for plotting
    stages = ['1', '2', '3', '4', '5', '5B']
    stage_labels = [
        '1: Stat. only',
        '2: SH0ES total',
        '3: + Parallax',
        '4: + Period',
        '5: + Metallicity\n+ Realistic σ',
        '5B: Conservative'
    ]

    h0_values = [
        73.17,  # Stage 1
        73.17,  # Stage 2
        72.17,  # Stage 3
        71.17,  # Stage 4
        70.17,  # Stage 5
        73.17   # Stage 5B
    ]

    sigma_values = [
        0.80,   # Stage 1
        1.31,   # Stage 2
        1.31,   # Stage 3
        1.31,   # Stage 4
        2.58,   # Stage 5
        2.58    # Stage 5B
    ]

    tension_values = [
        6.0,    # Stage 1
        4.1,    # Stage 2
        3.4,    # Stage 3
        2.7,    # Stage 4
        1.1,    # Stage 5
        2.2     # Stage 5B
    ]

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # X positions
    x_pos = np.arange(len(stages))

    # Plot Planck band (horizontal)
    ax.axhspan(PLANCK_H0 - PLANCK_SIGMA, PLANCK_H0 + PLANCK_SIGMA,
               alpha=0.2, color='blue', zorder=1, label='Planck 2018')
    ax.axhline(PLANCK_H0, color='blue', linestyle='--', linewidth=1.5,
               alpha=0.7, zorder=2)

    # Plot tension evolution
    colors = ['red', 'orange', 'gold', 'yellowgreen', 'green', 'purple']

    # Connect stages 1-5 with line
    ax.plot(x_pos[:5], h0_values[:5], 'o-', color='darkred', linewidth=2,
            markersize=8, zorder=3, label='Tension evolution')

    # Plot Stage 5B separately (conservative scenario)
    ax.plot(x_pos[5], h0_values[5], 'o', color='purple', markersize=10,
            zorder=3, label='Conservative (no corrections)')

    # Error bars
    for i in range(len(stages)):
        ax.errorbar(x_pos[i], h0_values[i], yerr=sigma_values[i],
                   fmt='o', color=colors[i], markersize=8, capsize=5,
                   capthick=2, linewidth=2, zorder=4)

        # Add tension value labels
        ax.text(x_pos[i], h0_values[i] + sigma_values[i] + 0.5,
               f'{tension_values[i]:.1f}σ',
               ha='center', va='bottom', fontsize=10, fontweight='bold',
               color=colors[i])

    # Add 3σ threshold line
    threshold_h0 = PLANCK_H0 + 3 * np.sqrt(PLANCK_SIGMA**2 + 2.58**2)
    ax.axhline(threshold_h0, color='red', linestyle=':', linewidth=1.5,
               alpha=0.5, label='3σ threshold')

    # Formatting
    ax.set_xlabel('Stage', fontsize=12, fontweight='bold')
    ax.set_ylabel('H₀ (km s⁻¹ Mpc⁻¹)', fontsize=12, fontweight='bold')
    ax.set_title('Tension Evolution: Progressive Reduction Through Realistic Systematics',
                fontsize=14, fontweight='bold', pad=20)

    ax.set_xticks(x_pos)
    ax.set_xticklabels(stage_labels, fontsize=9)
    ax.set_ylim(64, 77)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Legend
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

    # Add annotations
    ax.text(0.02, 0.98,
           f'Planck: H₀ = {PLANCK_H0:.2f} ± {PLANCK_SIGMA:.2f} km s⁻¹ Mpc⁻¹',
           transform=ax.transAxes, fontsize=9, va='top',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

    ax.text(0.98, 0.02,
           f'Tension reduction: 6.0σ → 1.1σ\nConservative: 6.0σ → 2.2σ',
           transform=ax.transAxes, fontsize=9, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    plt.tight_layout()

    # Save both PNG and PDF
    plt.savefig('figures/figure1_tension_evolution.png', dpi=300, bbox_inches='tight')
    plt.savefig('figures/figure1_tension_evolution.pdf', bbox_inches='tight')

    print("✅ Figure 1 generated successfully:")
    print("   - figures/figure1_tension_evolution.png (300 DPI)")
    print("   - figures/figure1_tension_evolution.pdf")

    plt.close()

if __name__ == '__main__':
    create_tension_evolution_figure()
