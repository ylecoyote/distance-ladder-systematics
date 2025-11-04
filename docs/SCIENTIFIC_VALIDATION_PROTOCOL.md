# Scientific Validation Protocol

**Purpose**: Comprehensive validation methodology for scientific rigor of the distance ladder systematics manuscript

**Created**: 2025-11-02
**Status**: Production validation framework
**Apply to**: Final manuscript before submission, after major revisions, or on reviewer request

---

## Overview

This protocol validates four critical dimensions of scientific manuscripts:
1. **Computational Reproducibility**: Can results be regenerated from code?
2. **Mathematical Correctness**: Are derivations algebraically sound?
3. **Statistical Validity**: Do correlation matrices and chi-square calculations check out?
4. **Numerical Consistency**: Are values consistent across text, tables, and figures?

---

## Phase 1: Computational Reproducibility

**Goal**: Execute all analysis scripts and verify outputs match manuscript claims

### Scripts to Execute

1. **Error Budget Calculation**
   ```bash
   python analysis/calculate_error_budget_correlated.py
   ```
   **Verify**: Output matches Table 1 systematic budget values

2. **Joint Bias Correction Fit**
   ```bash
   python analysis/joint_bias_correction_fit.py
   ```
   **Verify**:
   - Output H₀ = 70.17 ± 3.24 km/s/Mpc
   - Matches manuscript §3.1 endpoint

3. **2D Correlation Sensitivity**
   ```bash
   python analysis/create_2d_contour_sensitivity.py
   ```
   **Verify**: Output matches Figure 3 contour levels

4. **Period Histogram**
   ```bash
   python analysis/create_period_histogram.py
   ```
   **Verify**: Output matches Figure 2 distributions

### Validation Checklist

- [ ] All scripts execute without errors
- [ ] Output values match manuscript within rounding
- [ ] Figures regenerate identically to manuscript versions
- [ ] Data files in `data/` directory are correctly formatted
- [ ] No hardcoded values that should come from calculations

---

## Phase 2: Mathematical Derivations

**Goal**: Re-derive key equations and verify algebraic correctness

### Derivations to Verify

#### 2.1 Parallax Bias Correction

**Equation**: ΔH₀/H₀ ≈ -0.4605 Δϖ/ϖ
**Given**: Δϖ = +0.017 mas, ϖ̄ = 0.743 mas
**Expected**: ΔH₀/H₀ ≈ -1.05%

**Re-derivation**:
```
μ = 5 log₁₀(d/10 pc) = -5 log₁₀(ϖ/mas) + 10
∂μ/∂ϖ = -5/(ϖ ln 10)
Δμ ≈ -5 Δϖ/(ϖ ln 10) = -5(0.017)/(0.743 × 2.303) = -0.050 mag
ΔH₀/H₀ = -0.4605 Δμ = -0.4605 × (-0.050) = +0.023 ≈ +2.3%

Wait - check sign convention!
With ϖ_true = ϖ_Gaia + Δϖ (positive zero-point):
Δμ = +5 Δϖ/(ϖ ln 10) = +0.050 mag (distances too short)
ΔH₀/H₀ = -0.4605 × (+0.050) = -0.023 ≈ -2.3% (H₀ too high)

But manuscript uses dilution factor 60%:
ΔH₀_diluted ≈ 0.60 × (-2.3%) ≈ -1.4% ≈ -1.0 km/s/Mpc at H₀ = 73
```

**Verify**: Matches manuscript §2.1.1 adopted correction of -1.0 km/s/Mpc

#### 2.2 Period-Luminosity Break Bias

**Equation**: ΔH₀/H₀ ≈ -0.4605 Δμ
**Given**: Δβ = +0.5, Δ⟨log P⟩ = 0.15 days
**Expected**: ΔH₀ ≈ +1.0 km/s/Mpc after dilution

**Re-derivation**:
```
Δμ = Δβ × Δ⟨log P⟩ = 0.5 × 0.15 = +0.075 mag
ΔH₀/H₀ = -0.4605 × 0.075 = -0.0345 ≈ -3.45%
At H₀ = 73: ΔH₀ = -3.45% × 73 = -2.5 km/s/Mpc

With 40% MW anchor fraction (dilution):
ΔH₀_diluted ≈ 0.40 × (-2.5) = -1.0 km/s/Mpc
```

**Verify**: Matches manuscript §2.1.1 adopted correction

#### 2.3 Tension Calculation

**Stage 1**: σ_stat = 0.80, σ_Planck = 0.54, Δ = 5.81
```
σ_combined = √(0.80² + 0.54²) = √(0.64 + 0.2916) = √0.9316 ≈ 0.965
Tension = 5.81 / 0.965 ≈ 6.02σ ≈ 6.0σ
```

**Stage 5**: σ_total = 3.24, σ_Planck = 0.54, Δ = 2.81
```
σ_combined = √(3.24² + 0.54²) = √(10.4976 + 0.2916) = √10.7892 ≈ 3.285
Tension = 2.81 / 3.285 ≈ 0.855σ ≈ 0.86σ
```

**Verify**: Matches Table 2 and Figure 1 caption

#### 2.4 Correlated Systematic Uncertainty

**Given**: 10 systematic sources with correlation matrix R
**Individual**: σ_uncorr = √(Σᵢ σᵢ²) = 2.45 km/s/Mpc
**Correlated**: σ_corr = √(σᵀ R σ)

**Re-derivation**:
```python
import numpy as np

# Systematic budget from Table 1
sigma = np.array([1.31, 1.20, 0.95, 0.80, 0.65, 0.60, 0.50, 0.45, 0.35, 0.25])

# Uncorrelated
sigma_uncorr = np.sqrt(np.sum(sigma**2))
# Expected: 2.45 km/s/Mpc

# Correlated (requires correlation matrix R)
R = np.loadtxt('data/correlation_matrix.csv')
sigma_corr = np.sqrt(sigma @ R @ sigma)
# Expected: 3.14 km/s/Mpc
```

**Verify**: Matches manuscript §2.1.2 and §3.1

---

## Phase 3: Statistical Validation

**Goal**: Verify correlation matrices are valid and chi-square calculations are correct

### 3.1 Correlation Matrix Properties

**File**: `data/correlation_matrix.csv`

**Validation Code**:
```python
import numpy as np

# Load correlation matrix
R = np.loadtxt('data/correlation_matrix.csv', delimiter=',')

# Check 1: Symmetric
assert np.allclose(R, R.T), "Correlation matrix not symmetric!"

# Check 2: Diagonal is 1
assert np.allclose(np.diag(R), 1.0), "Diagonal elements not 1!"

# Check 3: Off-diagonal in [-1, 1]
off_diag = R[~np.eye(R.shape[0], dtype=bool)]
assert np.all(off_diag >= -1) and np.all(off_diag <= 1), "Off-diagonal out of bounds!"

# Check 4: Positive semi-definite (all eigenvalues ≥ 0)
eigenvalues = np.linalg.eigvals(R)
print(f"Eigenvalues: {eigenvalues}")
assert np.all(eigenvalues >= -1e-10), f"Negative eigenvalue found: {eigenvalues.min()}"

# Check 5: Cholesky decomposition exists
try:
    L = np.linalg.cholesky(R)
    print("✓ Cholesky decomposition successful")
except np.linalg.LinAlgError:
    raise AssertionError("Cholesky decomposition failed - matrix not positive definite!")

# Report condition number
cond = np.linalg.cond(R)
print(f"Condition number: {cond:.2f}")
if cond > 100:
    print("⚠️  Warning: High condition number - matrix near-singular")
```

**Expected Results**:
- Symmetry: Pass
- Diagonal: All 1.0
- Eigenvalues: All ≥ 0 (manuscript reports λ_min = 0.05)
- Cholesky: Success
- Condition number: Moderate (< 100)

### 3.2 Three-Method Convergence Chi-Square

**Measurements**:
- JAGB: H₀ = 67.96 ± 2.65 km/s/Mpc
- Cosmic Chronometers: H₀ = 68.33 ± 1.57 km/s/Mpc
- Planck CMB: H₀ = 67.36 ± 0.54 km/s/Mpc

**Weighted Mean Calculation**:
```python
import numpy as np

# Data
H0 = np.array([67.96, 68.33, 67.36])
sigma = np.array([2.65, 1.57, 0.54])

# Inverse-variance weights
weights = 1 / sigma**2
w_norm = weights / np.sum(weights)

# Weighted mean
H0_mean = np.sum(w_norm * H0)
sigma_mean = 1 / np.sqrt(np.sum(weights))

print(f"H₀ weighted mean: {H0_mean:.2f} ± {sigma_mean:.2f} km/s/Mpc")
# Expected: 67.48 ± 0.50

# Chi-square calculation
chi2 = np.sum(weights * (H0 - H0_mean)**2)
dof = len(H0) - 1  # 3 measurements - 1 parameter = 2 DOF
chi2_red = chi2 / dof

print(f"χ² = {chi2:.2f}")
print(f"χ²_red = {chi2_red:.2f}")
# Expected: χ²_red ≈ 0.19

# Planck weight
planck_weight = w_norm[2]
print(f"Planck weight: {planck_weight:.1%}")
# Expected: 86%
```

**Verify**:
- H₀_mean = 67.48 ± 0.50 (matches Table 3)
- χ²_red = 0.19 (matches Figure 4 caption and Table 3)
- Planck weight = 86% (matches Figure 4 caption)

### 3.3 Stage-5 Tension Consistency

**Validation Code**:
```python
import numpy as np

# Corrected Cepheid endpoint
H0_cepheid = 70.17
sigma_stat = 0.80
sigma_sys = 3.14  # correlated systematics
sigma_total = np.sqrt(sigma_stat**2 + sigma_sys**2)

print(f"σ_total = {sigma_total:.2f} km/s/Mpc")
# Expected: 3.24

# Planck
H0_planck = 67.36
sigma_planck = 0.54

# Combined uncertainty
delta = abs(H0_cepheid - H0_planck)
sigma_combined = np.sqrt(sigma_total**2 + sigma_planck**2)
tension = delta / sigma_combined

print(f"Δ = {delta:.2f} km/s/Mpc")
print(f"σ_combined = {sigma_combined:.2f} km/s/Mpc")
print(f"Tension = {tension:.2f}σ")
# Expected: 0.86σ

assert np.isclose(tension, 0.86, atol=0.02), f"Tension mismatch: {tension:.2f} vs 0.86"
```

---

## Phase 4: Numerical Consistency Audit

**Goal**: Verify all numerical values are consistent across text, tables, and figures

### 4.1 Endpoint Values (H₀ = 70.17 ± 3.24, 0.86σ)

**Search Pattern**:
```bash
# Find all instances of endpoint values
grep -n "70\.17\|3\.24\|0\.86" manuscript/manuscript.tex

# Should find in:
# - Abstract (line ~105)
# - Results §3.1 (line ~385-399)
# - Discussion (line ~497)
# - Conclusions (line ~560)
# - Figure 4 caption (line ~638)
```

**Validation**:
- [ ] All instances use **correlated** values (3.24, 0.86σ)
- [ ] No orphaned **uncorrelated** values (2.58, 1.07σ) except in comparison context

### 4.2 Systematic Uncertainty Values

**Search Pattern**:
```bash
# Correlated systematics
grep -n "3\.14" manuscript/manuscript.tex
# Expected: §3.1 title, body

# Uncorrelated systematics (should only appear in comparison)
grep -n "2\.45" manuscript/manuscript.tex
# Expected: §3.1 comparison only
```

**Validation**:
- [ ] σ_sys = 3.14 km/s/Mpc (correlated) is primary value
- [ ] σ_sys = 2.45 km/s/Mpc (uncorrelated) only in comparison

### 4.3 Chi-Square Consistency

**Search Pattern**:
```bash
# All chi-square values
grep -n "chi.*red\|\\chi\^2" manuscript/manuscript.tex data/tables/table3_h0_compilation.tex
```

**Validation**:
- [ ] χ²_red = 0.19 for three-method convergence (Figure 4, Table 3, text)
- [ ] No instances of χ²_red = 0.31 (old incorrect value)

### 4.4 Tension Evolution (Table 2 vs Text)

**Locations to Check**:
- Abstract (Stage 1 → Stage 5)
- Table 2 (all 5 stages)
- Figure 1 caption
- §3.2 body text

**Expected Values**:
| Stage | σ_sys (km/s/Mpc) | σ_total (km/s/Mpc) | Tension |
|-------|------------------|-------------------|---------|
| 1 | 0.00 | 0.80 | 6.0σ |
| 2 | 1.31 | 1.52 | 3.9σ |
| 3 | 2.12 | 2.27 | 2.6σ |
| 4 | 2.45 | 2.58 | 2.3σ |
| 5 | 3.14 | 3.24 | 0.86σ |

### 4.5 Three-Method Mean Consistency

**Search Pattern**:
```bash
grep -n "67\.48\|67\.36\|67\.96\|68\.33" manuscript/manuscript.tex data/tables/table3_h0_compilation.tex
```

**Validation**:
- [ ] Weighted mean: 67.48 ± 0.50 (Table 3, §3.3, Figure 4)
- [ ] Planck: 67.36 ± 0.54 (consistent everywhere)
- [ ] JAGB: 67.96 ± 2.65 (consistent everywhere)
- [ ] Cosmic Chronometers: 68.33 ± 1.57 (consistent everywhere)

### 4.6 Anchor Weights (Table vs Text)

**File**: `data/tables/table_anchor_weights.tex`

**Expected**:
- MW: 60% weight, Δϖ = +0.017 mas, ΔH₀ ≈ +1.8 km/s/Mpc
- LMC: 25% weight, geometric, ΔH₀ = 0.0
- NGC 4258: 15% weight, maser, ΔH₀ = 0.0
- **Diluted**: +1.1 km/s/Mpc
- **Adopted correction**: -1.0 km/s/Mpc

**Validation**:
- [ ] Table anchor weights sum to 100%
- [ ] Text in §2.1.1 matches table values
- [ ] Dilution factor consistent with 60% MW contribution

---

## DELVE Protocol for Validation

**When to use**: Complex manuscripts requiring multi-perspective validation

### Agent Roles

**Larrynator (λ)**: Logical rigor and mathematical correctness
- Execute Phase 2 (mathematical derivations)
- Verify algebraic steps
- Check dimensional analysis
- Validate sign conventions

**Curlytron (ξ)**: Novel validation approaches and edge cases
- Identify unconventional failure modes
- Test boundary conditions
- Challenge implicit assumptions
- Propose alternative verification methods

**Moebot (ρ)**: Practical implementation and resource constraints
- Execute Phase 1 (computational reproducibility)
- Execute Phase 3 (statistical validation)
- Execute Phase 4 (numerical consistency)
- Assess time/effort tradeoffs

### DELVE Workflow

**Phase 1: Individual Analysis** (Parallel)
```bash
# Launch all three agents simultaneously
larrynator: "Re-derive all bias correction equations and verify algebraic correctness"
curlytron: "Identify edge cases and alternative validation approaches for manuscript claims"
moebot: "Execute all analysis scripts and verify numerical consistency across manuscript"
```

**Phase 2: Cross-Pollination**
- Larrynator challenges Curlytron's unconventional tests for mathematical rigor
- Curlytron questions Moebot's acceptance criteria for completeness
- Moebot grounds Larrynator's derivations in computational feasibility

**Phase 3: Synthesis**
- Integrate mathematical correctness (λ)
- Incorporate edge case coverage (ξ)
- Balance with practical constraints (ρ)

**Phase 4: Unified Validation Report**
- Combined findings
- Prioritized issues (critical → minor)
- Actionable recommendations

---

## Validation Checklist (Quick Reference)

### Pre-Submission Validation
- [ ] All scripts execute without errors
- [ ] All mathematical derivations verified
- [ ] Correlation matrix positive semi-definite
- [ ] Chi-square calculations correct
- [ ] Endpoint values consistent (70.17 ± 3.24, 0.86σ)
- [ ] Systematic uncertainties consistent (σ_sys = 3.14 correlated)
- [ ] Three-method mean matches calculation (67.48 ± 0.50)
- [ ] Table references compile correctly (no "Table ??")
- [ ] Figure captions match computed values
- [ ] Sign conventions unified throughout

### Post-Revision Validation
- [ ] Changed values propagated to all locations
- [ ] New calculations verified independently
- [ ] Updated tables match updated text
- [ ] Figure captions updated if data changed
- [ ] No orphaned old values in Discussion/Conclusions

### Reviewer-Requested Validation
- [ ] Specific calculation requested by reviewer reproduced
- [ ] Alternative approach tested if suggested
- [ ] Sensitivity analysis performed if questioned
- [ ] Response letter claims match manuscript updates

---

## Automated Validation Scripts

### validate_all.sh
```bash
#!/bin/bash
# Comprehensive validation script

echo "=== Phase 1: Computational Reproducibility ==="
python analysis/calculate_error_budget_correlated.py || exit 1
python analysis/joint_bias_correction_fit.py || exit 1
python analysis/create_2d_contour_sensitivity.py || exit 1

echo "=== Phase 3: Statistical Validation ==="
python scripts/validate_correlation_matrix.py || exit 1
python scripts/validate_chi_square.py || exit 1
python scripts/validate_tension.py || exit 1

echo "=== Phase 4: Numerical Consistency ==="
bash scripts/audit_endpoint_values.sh || exit 1
bash scripts/audit_chi_square.sh || exit 1

echo "✓ All validation checks passed!"
```

### validate_correlation_matrix.py
```python
#!/usr/bin/env python3
"""Validate correlation matrix properties"""

import numpy as np
import sys

# Load correlation matrix
R = np.loadtxt('data/correlation_matrix.csv', delimiter=',')

# Checks
checks = []

# 1. Symmetric
checks.append(("Symmetric", np.allclose(R, R.T)))

# 2. Diagonal is 1
checks.append(("Diagonal = 1", np.allclose(np.diag(R), 1.0)))

# 3. Positive semi-definite
eigenvalues = np.linalg.eigvals(R)
checks.append(("Positive semi-definite", np.all(eigenvalues >= -1e-10)))

# 4. Cholesky decomposition
try:
    L = np.linalg.cholesky(R)
    checks.append(("Cholesky decomposition", True))
except np.linalg.LinAlgError:
    checks.append(("Cholesky decomposition", False))

# Report
print("Correlation Matrix Validation:")
for name, passed in checks:
    status = "✓" if passed else "✗"
    print(f"  {status} {name}")

# Exit code
if all(passed for _, passed in checks):
    print("\n✓ All checks passed")
    sys.exit(0)
else:
    print("\n✗ Some checks failed")
    sys.exit(1)
```

### validate_chi_square.py
```python
#!/usr/bin/env python3
"""Validate three-method convergence chi-square"""

import numpy as np
import sys

# Three-method measurements
H0 = np.array([67.96, 68.33, 67.36])  # JAGB, CC, Planck
sigma = np.array([2.65, 1.57, 0.54])

# Inverse-variance weights
weights = 1 / sigma**2
H0_mean = np.sum(weights * H0) / np.sum(weights)

# Chi-square
chi2 = np.sum(weights * (H0 - H0_mean)**2)
dof = len(H0) - 1
chi2_red = chi2 / dof

# Expected values
expected_mean = 67.48
expected_chi2_red = 0.19

# Validate
checks = [
    ("H₀ mean", np.isclose(H0_mean, expected_mean, atol=0.01)),
    ("χ²_red", np.isclose(chi2_red, expected_chi2_red, atol=0.01))
]

print("Chi-Square Validation:")
for name, passed in checks:
    status = "✓" if passed else "✗"
    print(f"  {status} {name}")

if all(passed for _, passed in checks):
    print(f"\n✓ H₀ = {H0_mean:.2f} km/s/Mpc")
    print(f"✓ χ²_red = {chi2_red:.2f}")
    sys.exit(0)
else:
    print(f"\n✗ H₀ = {H0_mean:.2f} (expected {expected_mean})")
    print(f"✗ χ²_red = {chi2_red:.2f} (expected {expected_chi2_red})")
    sys.exit(1)
```

### validate_tension.py
```python
#!/usr/bin/env python3
"""Validate Stage-5 tension calculation"""

import numpy as np
import sys

# Stage 5 endpoint
H0_cepheid = 70.17
sigma_stat = 0.80
sigma_sys = 3.14
sigma_total = np.sqrt(sigma_stat**2 + sigma_sys**2)

# Planck
H0_planck = 67.36
sigma_planck = 0.54

# Tension
delta = abs(H0_cepheid - H0_planck)
sigma_combined = np.sqrt(sigma_total**2 + sigma_planck**2)
tension = delta / sigma_combined

# Expected
expected_sigma_total = 3.24
expected_tension = 0.86

# Validate
checks = [
    ("σ_total", np.isclose(sigma_total, expected_sigma_total, atol=0.01)),
    ("Tension", np.isclose(tension, expected_tension, atol=0.02))
]

print("Tension Validation:")
for name, passed in checks:
    status = "✓" if passed else "✗"
    print(f"  {status} {name}")

if all(passed for _, passed in checks):
    print(f"\n✓ σ_total = {sigma_total:.2f} km/s/Mpc")
    print(f"✓ Tension = {tension:.2f}σ")
    sys.exit(0)
else:
    print(f"\n✗ σ_total = {sigma_total:.2f} (expected {expected_sigma_total})")
    print(f"✗ Tension = {tension:.2f}σ (expected {expected_tension})")
    sys.exit(1)
```

---

## Success Criteria

**Validation passes if**:
1. All computational scripts execute and match manuscript values
2. All mathematical derivations are algebraically correct
3. Correlation matrix is positive semi-definite with valid Cholesky decomposition
4. Chi-square calculations match reported values within rounding
5. Endpoint values consistent across all manuscript locations
6. No orphaned old values from previous revisions

**Validation fails if**:
- Scripts produce different values than manuscript
- Mathematical errors found in derivations
- Correlation matrix not positive semi-definite
- Chi-square mismatch > 0.02
- Inconsistent endpoint values across sections
- Old values still present in text/tables/figures

---

## Revision History

| Date | Version | Changes |
|------|---------|---------|
| 2025-11-02 | 1.0 | Initial protocol creation |

---

**Status**: Production ready
**Recommended usage**: Before every submission and after major revisions
**Estimated time**: 2-3 hours for full DELVE protocol validation
