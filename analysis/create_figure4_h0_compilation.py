#!/usr/bin/env python3
"""
Generate Figure 4: H₀ Compilation Forest Plot
Shows multiple H₀ measurements with convergence band

Data source: data/h0_measurements_compilation.csv
Output: figures/figure4_h0_compilation.png (publication quality)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_h0_compilation_figure():
    """Create publication-quality H₀ compilation forest plot"""

    # Load data
    data = pd.read_csv('data/h0_measurements_compilation.csv')

    # Sort by H₀ value (ascending)
    data = data.sort_values('H0_km_s_Mpc', ascending=True)

    # Exclude weighted mean from main plot (will show as band)
    weighted_mean_data = data[data['Method'] == 'Weighted Mean'].iloc[0]
    plot_data = data[data['Method'] != 'Weighted Mean'].copy()

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 7))

    # Y positions for each method
    y_pos = np.arange(len(plot_data))

    # Color scheme by category
    color_map = {
        'Early Universe': 'blue',
        'Distance Ladder': 'red',
        'Model-Independent': 'green',
        'Convergence': 'purple'
    }

    # Marker size based on precision (larger = more precise)
    marker_sizes = 150 / plot_data['Sigma_km_s_Mpc'].values

    # Track categories for legend
    plotted_categories = set()

    # Plot each measurement
    for i, (idx, row) in enumerate(plot_data.iterrows()):
        color = color_map.get(row['Category'], 'gray')

        # Horizontal error bar
        label = row['Category'] if row['Category'] not in plotted_categories else ""
        if label:
            plotted_categories.add(label)

        ax.errorbar(row['H0_km_s_Mpc'], y_pos[i],
                   xerr=row['Sigma_km_s_Mpc'],
                   fmt='o', color=color,
                   markersize=marker_sizes[i]/10,
                   capsize=5, capthick=2, linewidth=2,
                   label=label)

        # Highlight Cepheid (shares systematics)
        if row['Shares_Systematics_With_Cepheid']:
            ax.plot(row['H0_km_s_Mpc'], y_pos[i], 'o',
                   markerfacecolor='none', markeredgecolor='orange',
                   markersize=marker_sizes[i]/10 + 3, markeredgewidth=3,
                   zorder=10)

    # Add convergence band (weighted mean ± σ)
    convergence_h0 = weighted_mean_data['H0_km_s_Mpc']
    convergence_sigma = weighted_mean_data['Sigma_km_s_Mpc']

    ax.axvspan(convergence_h0 - convergence_sigma,
              convergence_h0 + convergence_sigma,
              alpha=0.2, color='gray', zorder=1,
              label='Three-method convergence')
    ax.axvline(convergence_h0, color='gray', linestyle='--',
              linewidth=2, alpha=0.7, zorder=2)

    # Add 3σ threshold lines
    threshold_lower = convergence_h0 - 3 * convergence_sigma
    threshold_upper = convergence_h0 + 3 * convergence_sigma
    ax.axvline(threshold_lower, color='red', linestyle=':',
              linewidth=1.5, alpha=0.5)
    ax.axvline(threshold_upper, color='red', linestyle=':',
              linewidth=1.5, alpha=0.5, label='3σ threshold')

    # Formatting
    ax.set_yticks(y_pos)
    ax.set_yticklabels(plot_data['Method'].values, fontsize=11)
    ax.set_xlabel('H₀ (km s⁻¹ Mpc⁻¹)', fontsize=12, fontweight='bold')
    ax.set_title('H₀ Measurements Compilation: Convergence at 67-68 km s⁻¹ Mpc⁻¹',
                fontsize=14, fontweight='bold', pad=20)

    ax.set_xlim(65, 76)
    ax.grid(True, alpha=0.3, axis='x', linestyle='--')

    # Add text annotations
    ax.text(convergence_h0, len(plot_data) - 0.5,
           f'Weighted mean:\n{convergence_h0:.2f} ± {convergence_sigma:.2f}',
           ha='center', va='bottom', fontsize=9,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # Add note about Cepheid
    ax.text(0.98, 0.02,
           'Orange circle: Shares systematics\nwith Cepheid distance ladder',
           transform=ax.transAxes, fontsize=9, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # Legend - remove duplicates
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(),
             loc='upper left', fontsize=10, framealpha=0.9)

    plt.tight_layout()

    # Save both PNG and PDF
    plt.savefig('figures/figure4_h0_compilation.png', dpi=300, bbox_inches='tight')
    plt.savefig('figures/figure4_h0_compilation.pdf', bbox_inches='tight')

    print("✅ Figure 4 generated successfully:")
    print("   - figures/figure4_h0_compilation.png (300 DPI)")
    print("   - figures/figure4_h0_compilation.pdf")
    print(f"   Convergence: H₀ = {convergence_h0:.2f} ± {convergence_sigma:.2f} km s⁻¹ Mpc⁻¹")

    plt.close()

if __name__ == '__main__':
    create_h0_compilation_figure()
