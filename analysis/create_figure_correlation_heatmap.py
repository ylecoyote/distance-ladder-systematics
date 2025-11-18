#!/usr/bin/env python3
"""
Generate Correlation Heatmap: Systematic Error Correlation Matrix Visualization
Shows 9×9 correlation matrix with color-coded correlation strengths

Data source: data/correlation_matrix_updated.csv
Output: figures/figure_correlation_heatmap.png (publication quality)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def create_correlation_heatmap():
    """Create publication-quality correlation matrix heatmap"""

    # Load correlation matrix
    corr_matrix = pd.read_csv('data/correlation_matrix_updated.csv',
                              comment='#', index_col=0)

    # Create figure with appropriate size
    fig, ax = plt.subplots(figsize=(12, 10))

    # Create custom colormap (white for 0, blue for positive correlations)
    colors = ['white', 'lightblue', 'cornflowerblue', 'royalblue', 'darkblue']
    n_bins = 100
    cmap = LinearSegmentedColormap.from_list('correlation', colors, N=n_bins)

    # Plot heatmap
    im = ax.imshow(corr_matrix.values, cmap=cmap, vmin=0, vmax=1,
                   aspect='auto', interpolation='nearest')

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label('Correlation Coefficient (ρ)', rotation=270,
                   labelpad=20, fontsize=12, fontweight='bold')

    # Set tick labels
    ax.set_xticks(np.arange(len(corr_matrix.columns)))
    ax.set_yticks(np.arange(len(corr_matrix.index)))

    # Shorter labels for better readability
    short_labels = [
        'Parallax ZP',
        'Period Dist.',
        'Metallicity',
        'Crowding',
        'Photometry',
        'Extinction',
        'LMC Distance',
        'NGC4258',
        'SNe Ia Std.'
    ]

    ax.set_xticklabels(short_labels, rotation=45, ha='right', fontsize=10)
    ax.set_yticklabels(short_labels, fontsize=10)

    # Add correlation values as text annotations
    for i in range(len(corr_matrix.index)):
        for j in range(len(corr_matrix.columns)):
            value = corr_matrix.values[i, j]
            # Only show non-zero correlations and skip diagonal
            if value != 0.0 and i != j:
                text_color = 'white' if value > 0.5 else 'black'
                ax.text(j, i, f'{value:.1f}',
                       ha='center', va='center', color=text_color,
                       fontsize=9, fontweight='bold')
            elif i == j:
                # Show diagonal as 1.0
                ax.text(j, i, '1.0',
                       ha='center', va='center', color='white',
                       fontsize=8)

    # Add grid lines between cells
    ax.set_xticks(np.arange(len(corr_matrix.columns)) - 0.5, minor=True)
    ax.set_yticks(np.arange(len(corr_matrix.index)) - 0.5, minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
    ax.tick_params(which='minor', size=0)

    # Title
    ax.set_title('Systematic Error Correlation Matrix (9×9 Updated)\n' +
                'Key Correlations: Metallicity-Extinction (0.3), Period-Metallicity (0.3)',
                fontsize=14, fontweight='bold', pad=20)

    # Add annotation boxes for key correlations
    ax.text(0.02, 0.98,
           'Strong correlations:\n• Metallicity ↔ Extinction: ρ = 0.3\n' +
           '• Period ↔ Metallicity: ρ = 0.3\n' +
           '• Crowding ↔ Extinction: ρ = 0.3',
           transform=ax.transAxes, fontsize=9, va='top',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    ax.text(0.98, 0.02,
           'Correlation impact:\n' +
           'Off-diagonal: 0.81 (km/s/Mpc)²\n' +
           'Inflates σ_sys by 18%\n' +
           '(from 1.45 to 1.71 km/s/Mpc)',
           transform=ax.transAxes, fontsize=9, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    plt.tight_layout()

    # Save both PNG and PDF
    plt.savefig('figures/figure_correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.savefig('figures/figure_correlation_heatmap.pdf', bbox_inches='tight')

    print("✅ Correlation heatmap generated successfully:")
    print("   - figures/figure_correlation_heatmap.png (300 DPI)")
    print("   - figures/figure_correlation_heatmap.pdf")
    print(f"   Matrix size: {corr_matrix.shape[0]}×{corr_matrix.shape[1]}")

    # Print non-zero correlations
    print("\n   Non-zero correlations:")
    for i in range(len(corr_matrix.index)):
        for j in range(i+1, len(corr_matrix.columns)):
            if corr_matrix.values[i, j] != 0.0:
                print(f"   • {short_labels[i]} ↔ {short_labels[j]}: {corr_matrix.values[i, j]:.1f}")

    plt.close()

if __name__ == '__main__':
    create_correlation_heatmap()
