#!/usr/bin/env python3
"""
Generate Figure 2: Systematic Error Budget Comparison

Creates stacked bar chart comparing SH0ES vs Our Assessment of systematic errors.

Author: Distance Ladder Systematics Project
Date: October 22, 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =============================================================================
# Configuration
# =============================================================================

# Publication-quality settings
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['axes.linewidth'] = 1.2

# =============================================================================
# Load Data
# =============================================================================

data_dir = Path(__file__).parent.parent / "data"
error_budget = pd.read_csv(data_dir / "systematic_error_budget.csv")

# Exclude statistical uncertainty (separate category)
systematic_only = error_budget[error_budget['Error_Source'] != 'Statistical_Uncertainty'].copy()

# =============================================================================
# Prepare Data for Stacked Bar Chart
# =============================================================================

# Sort by our assessment (largest first) for better visualization
systematic_only = systematic_only.sort_values('Our_Assessment_km_s_Mpc', ascending=False)

sources = systematic_only['Error_Source'].str.replace('_', '\n').values  # Line breaks for readability
shoes_values = systematic_only['SH0ES_Estimate_km_s_Mpc'].values
our_values = systematic_only['Our_Assessment_km_s_Mpc'].values

# Calculate totals
shoes_total = np.sqrt(np.sum(shoes_values**2))
our_total = np.sqrt(np.sum(our_values**2))

print(f"Creating Figure 2: Systematic Error Budget Comparison")
print(f"SH0ES total: {shoes_total:.2f} km/s/Mpc")
print(f"Our total:   {our_total:.2f} km/s/Mpc")
print()

# =============================================================================
# Create Stacked Bar Chart
# =============================================================================

fig, ax = plt.subplots(figsize=(10, 8))

# Define categories for color coding
categories = {
    'Parallax\nZero Point': 'Anchors',
    'Period\nDistribution': 'P-L Relation',
    'Metallicity\nCorrection': 'P-L Relation',
    'Crowding\nDirect': 'Photometry',
    'Crowding\nCovariant': 'Photometry',
    'Photometric\nCalibration': 'Photometry',
    'Extinction\nReddening': 'Photometry',
    'LMC\nDistance': 'Anchors',
    'NGC4258\nDistance': 'Anchors',
    'SNe Ia\nStandardization': 'Second Rung'
}

# Color scheme
colors = {
    'Anchors': '#E74C3C',  # Red
    'P-L Relation': '#3498DB',  # Blue
    'Photometry': '#F39C12',  # Orange
    'Second Rung': '#27AE60'  # Green
}

# Get colors for each source
source_colors = [colors.get(categories.get(s), '#95A5A6') for s in sources]  # Gray for uncategorized

# Create side-by-side grouped bars
x = np.arange(len(sources))
width = 0.35

bars1 = ax.bar(x - width/2, shoes_values, width, label='SH0ES',
               color='lightgray', edgecolor='black', linewidth=1.2)
bars2 = ax.bar(x + width/2, our_values, width, label='Our Assessment',
               color=source_colors, edgecolor='black', linewidth=1.2, alpha=0.8)

# Customize axes
ax.set_ylabel('Systematic Uncertainty (km/s/Mpc)', fontsize=14, fontweight='bold')
ax.set_title('Systematic Error Budget Comparison\nSH0ES vs Our Independent Assessment',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(sources, rotation=45, ha='right', fontsize=10)
ax.legend(fontsize=12, loc='upper right')
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add total bars
total_x = len(sources) + 0.5
ax.bar(total_x - width/2, shoes_total, width, color='darkgray',
       edgecolor='black', linewidth=1.5, hatch='///')
ax.bar(total_x + width/2, our_total, width, color='darkred',
       edgecolor='black', linewidth=1.5, hatch='///', alpha=0.8)
ax.text(total_x, -0.15, 'TOTAL\n(quadrature)', ha='center', fontsize=10, fontweight='bold')

# Add value labels on total bars
ax.text(total_x - width/2, shoes_total + 0.05, f'{shoes_total:.2f}',
        ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.text(total_x + width/2, our_total + 0.05, f'{our_total:.2f}',
        ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add factor difference annotation
factor = our_total / shoes_total
ax.text(total_x, our_total + 0.3, f'{factor:.2f}× larger',
        ha='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Set y-axis limit
ax.set_ylim(0, max(our_values.max(), our_total) * 1.15)

# Add category legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=colors[cat], edgecolor='black', label=cat, alpha=0.8)
                   for cat in ['Anchors', 'P-L Relation', 'Photometry', 'Second Rung']]
ax.legend(handles=legend_elements, title='Error Category',
          loc='upper left', fontsize=10, title_fontsize=11)

plt.tight_layout()

# Save figure
output_dir = Path(__file__).parent.parent / "figures"
output_dir.mkdir(exist_ok=True)
output_file = output_dir / "figure2_error_budget_comparison.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"Figure saved to: {output_file}")

# Also save as PDF for publication
output_file_pdf = output_dir / "figure2_error_budget_comparison.pdf"
plt.savefig(output_file_pdf, bbox_inches='tight')
print(f"PDF saved to: {output_file_pdf}")

plt.close()

# =============================================================================
# Create Alternative Version: Horizontal Stacked Bars
# =============================================================================

fig, ax = plt.subplots(figsize=(10, 6))

# Create data for stacked horizontal bars
shoes_data = shoes_values.copy()
our_data = our_values.copy()

categories_list = ['SH0ES', 'Our Assessment']
y_pos = np.arange(len(categories_list))

# Stacked horizontal bars
bottom_shoes = 0
bottom_ours = 0

for i, (source, shoes_val, our_val) in enumerate(zip(sources, shoes_data, our_data)):
    ax.barh(0, shoes_val**2, left=bottom_shoes, height=0.4,
            label=source.replace('\n', ' ') if i < 4 else None,
            color=source_colors[i], edgecolor='black', linewidth=0.8, alpha=0.8)
    ax.barh(1, our_val**2, left=bottom_ours, height=0.4,
            color=source_colors[i], edgecolor='black', linewidth=0.8, alpha=0.8)
    bottom_shoes += shoes_val**2
    bottom_ours += our_val**2

ax.set_yticks(y_pos)
ax.set_yticklabels(categories_list, fontsize=12)
ax.set_xlabel('Variance (km²/s²/Mpc²)', fontsize=12, fontweight='bold')
ax.set_title('Systematic Error Variance Breakdown (Stacked)', fontsize=14, fontweight='bold')
ax.legend(loc='upper right', fontsize=9, ncol=2)

# Add total uncertainty labels
ax.text(bottom_shoes + 0.2, 0, f'σ_sys = {shoes_total:.2f} km/s/Mpc',
        va='center', fontsize=11, fontweight='bold')
ax.text(bottom_ours + 0.2, 1, f'σ_sys = {our_total:.2f} km/s/Mpc',
        va='center', fontsize=11, fontweight='bold')

plt.tight_layout()

output_file_alt = output_dir / "figure2_error_budget_stacked.png"
plt.savefig(output_file_alt, dpi=300, bbox_inches='tight')
print(f"Alternative figure saved to: {output_file_alt}")

plt.close()

print()
print("=" * 60)
print("FIGURE 2 GENERATION COMPLETE")
print("=" * 60)
