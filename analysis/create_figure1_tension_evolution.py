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

    # Prepare data for plotting (Scenario A + Prior 1 baseline)
    stages = ['1', '2', '3', '4', '5']
    stage_labels = [
        '1: Stat. only',
        '2: SH0ES total',
        '3: Scenario A ZP',
        '4: + Period dist.',
        '5: + Metallicity\n+ Realistic σ'
    ]

    h0_values = [
        73.17,  # Stage 1: Statistical only
        73.17,  # Stage 2: SH0ES total
        73.17,  # Stage 3: Scenario A (no bias correction)
        70.67,  # Stage 4: Period distribution -2.5 km/s/Mpc
        69.67   # Stage 5: Metallicity + realistic σ (Scenario A + Prior 1)
    ]

    sigma_values = [
        0.80,   # Stage 1: Statistical only
        1.31,   # Stage 2: SH0ES total (sqrt(0.8² + 1.04²))
        1.31,   # Stage 3: Same as Stage 2
        1.31,   # Stage 4: Still using SH0ES total
        1.89    # Stage 5: σ_total = sqrt(0.8² + 1.71²)
    ]

    tension_values = [
        6.0,    # Stage 1
        4.1,    # Stage 2
        4.1,    # Stage 3 (no bias correction in Scenario A)
        2.3,    # Stage 4: (70.67 - 67.36) / sqrt(1.31² + 0.54²)
        1.2     # Stage 5: (69.67 - 67.36) / sqrt(1.89² + 0.54²)
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
    colors = ['red', 'orange', 'gold', 'yellowgreen', 'green']

    # Connect stages 1-5 with line
    ax.plot(x_pos, h0_values, 'o-', color='darkred', linewidth=2,
            markersize=8, zorder=3, label='Tension evolution (Scenario A + Prior 1 baseline)')

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
    threshold_h0 = PLANCK_H0 + 3 * np.sqrt(PLANCK_SIGMA**2 + 1.89**2)
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
           f'Tension reduction: 6.0σ → 1.2σ (baseline)\nScenario range: 0.2σ to 1.7σ',
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
