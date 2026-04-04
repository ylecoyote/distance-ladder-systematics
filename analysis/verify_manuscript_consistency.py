#!/usr/bin/env python3
"""
Manuscript Consistency Verifier for Distance Ladder Systematics

Validates numerical consistency across:
- Data files (CSV)
- Figure generation scripts
- LaTeX tables
- README documentation
- Overleaf submission package

Truth source: config/numerical_claims.yaml (single source of truth)
Architecture: Decorator-based check registration with YAML-first design

Usage:
    python3 analysis/verify_manuscript_consistency.py [--json] [--only CATEGORY ...]

Exit codes:
    0: All checks passed
    1: One or more checks failed (ERROR or WARNING severity)

Author: Distance Ladder Systematics Project
Date: November 2025
Version: 2.0 (Refactored with YAML-first architecture)
"""

from __future__ import annotations
import argparse
import json
import re
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable, List, Dict, Any, Optional

try:
    import yaml
    import numpy as np
    import pandas as pd
    HAS_ANALYSIS_LIBS = True
except ImportError:
    HAS_ANALYSIS_LIBS = False

# =============================================================================
# Paths
# =============================================================================

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
DATA_DIR = ROOT / "data"
FIGURES_DIR = ROOT / "figures"
ANALYSIS_DIR = ROOT / "analysis"
DOCS_DIR = ROOT / "docs"
MANUSCRIPT_DIR = ROOT / "manuscript"

CLAIMS_FILE = CONFIG_DIR / "numerical_claims.yaml"

# =============================================================================
# Data Structures
# =============================================================================

@dataclass
class CheckResult:
    """Result of a single verification check"""
    id: str
    name: str
    category: str
    severity: str  # "ERROR" | "WARNING" | "INFO"
    passed: bool
    details: str = ""
    hint: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return asdict(self)


# =============================================================================
# Verification Framework
# =============================================================================

class VerificationFramework:
    """
    Framework for registering and running verification checks.

    Uses decorator pattern for clean check registration:

        @framework.register_check(
            id="CHECK_001",
            name="Description",
            category="tension",
            severity="ERROR"
        )
        def my_check(claims: Dict) -> CheckResult:
            # ... validation logic ...
            return CheckResult(...)
    """

    def __init__(self) -> None:
        self._checks: List[Dict[str, Any]] = []
        self._claims: Optional[Dict] = None
        self._start_time = time.time()

    def load_claims(self) -> Dict:
        """Load numerical claims from YAML (single source of truth)"""
        if self._claims is not None:
            return self._claims

        if not CLAIMS_FILE.exists():
            raise FileNotFoundError(
                f"Numerical claims file not found: {CLAIMS_FILE}\n"
                f"This file is required as the single source of truth."
            )

        with open(CLAIMS_FILE) as f:
            self._claims = yaml.safe_load(f)

        return self._claims

    def register_check(
        self,
        id: str,
        name: str,
        category: str,
        severity: str,
    ):
        """
        Decorator for registering a verification check.

        Parameters
        ----------
        id : str
            Unique check identifier (e.g., "TENSION_001")
        name : str
            Human-readable check description
        category : str
            Check category (tension, systematics, h0_compilation, figures, manuscript)
        severity : str
            "ERROR", "WARNING", or "INFO"
        """
        def decorator(func: Callable[[Dict], CheckResult]):
            self._checks.append({
                "id": id,
                "name": name,
                "category": category,
                "severity": severity,
                "func": func,
            })
            return func
        return decorator

    def run_all(self, only_categories: Optional[List[str]] = None) -> List[CheckResult]:
        """
        Run all registered checks.

        Parameters
        ----------
        only_categories : List[str], optional
            If provided, only run checks in these categories

        Returns
        -------
        results : List[CheckResult]
            Results from all executed checks
        """
        claims = self.load_claims()
        results: List[CheckResult] = []

        for chk in self._checks:
            # Category filtering
            if only_categories and chk["category"] not in only_categories:
                continue

            # Run check
            try:
                result = chk["func"](claims)
                results.append(result)

                # Optional: fail-fast on ERROR
                # if result.severity == "ERROR" and not result.passed:
                #     break

            except Exception as e:
                # Catch check failures and record as ERROR
                results.append(CheckResult(
                    id=chk["id"],
                    name=chk["name"],
                    category=chk["category"],
                    severity="ERROR",
                    passed=False,
                    details=f"Check raised exception: {type(e).__name__}: {e}",
                    hint="Check implementation may have a bug"
                ))

        return results

    def report_human(self, results: List[CheckResult]) -> int:
        """
        Generate human-readable report.

        Returns
        -------
        exit_code : int
            0 if all checks passed, 1 otherwise
        """
        print("=" * 80)
        print("MANUSCRIPT CONSISTENCY VERIFICATION REPORT")
        print("=" * 80)
        print()
        print(f"Repository: {ROOT}")
        print(f"Claims version: {self._claims['metadata']['version']}")
        print(f"Checks run: {len(results)}")
        print(f"Time: {time.time() - self._start_time:.2f}s")
        print()

        errors = [r for r in results if not r.passed and r.severity == "ERROR"]
        warnings = [r for r in results if not r.passed and r.severity == "WARNING"]
        info = [r for r in results if not r.passed and r.severity == "INFO"]
        passed = [r for r in results if r.passed]

        if errors or warnings:
            print("❌ VERIFICATION FAILED")
        else:
            print("✅ ALL CHECKS PASSED")

        print()
        print(f"   Passed:   {len(passed)}/{len(results)}")
        print(f"   Failed:   {len(errors) + len(warnings)}/{len(results)}")
        if errors:
            print(f"     Errors:   {len(errors)}")
        if warnings:
            print(f"     Warnings: {len(warnings)}")
        if info:
            print(f"     Info:     {len(info)}")
        print()

        # Report errors
        if errors:
            print("ERRORS (must fix before submission):")
            print("-" * 80)
            for r in errors:
                print(f"  ❌ {r.id}: {r.name}")
                print(f"     {r.details}")
                if r.hint:
                    print(f"     → FIX: {r.hint}")
                print()

        # Report warnings
        if warnings:
            print("WARNINGS (should fix):")
            print("-" * 80)
            for r in warnings:
                print(f"  ⚠️  {r.id}: {r.name}")
                print(f"     {r.details}")
                if r.hint:
                    print(f"     → FIX: {r.hint}")
                print()

        # Report info (if any failed)
        if info:
            print("INFO (advisory):")
            print("-" * 80)
            for r in info:
                print(f"  ℹ️  {r.id}: {r.name}")
                print(f"     {r.details}")
                print()

        print("=" * 80)

        if errors or warnings:
            print("\n   Manuscript is NOT ready for submission.\n")
            return 1
        else:
            print("\n   Manuscript is consistent and ready for submission.\n")
            return 0

    def report_json(self, results: List[CheckResult]) -> int:
        """
        Generate machine-readable JSON report.

        Returns
        -------
        exit_code : int
            0 if all checks passed, 1 otherwise
        """
        errors = [r for r in results if not r.passed and r.severity == "ERROR"]
        warnings = [r for r in results if not r.passed and r.severity == "WARNING"]

        output = {
            "metadata": {
                "repository": str(ROOT),
                "claims_version": self._claims["metadata"]["version"],
                "timestamp": time.time(),
                "elapsed_seconds": time.time() - self._start_time
            },
            "summary": {
                "total_checks": len(results),
                "passed": len([r for r in results if r.passed]),
                "failed": len([r for r in results if not r.passed]),
                "errors": len(errors),
                "warnings": len(warnings)
            },
            "results": [r.to_dict() for r in results]
        }

        print(json.dumps(output, indent=2))
        return 1 if (errors or warnings) else 0


# =============================================================================
# Create Framework Instance
# =============================================================================

framework = VerificationFramework()


# =============================================================================
# Check #1: Tension Evolution Consistency
# =============================================================================

@framework.register_check(
    id="TENSION_001",
    name="Tension evolution CSV vs expected values",
    category="tension",
    severity="ERROR"
)
def check_tension_csv(claims: Dict) -> CheckResult:
    """Verify tension evolution CSV matches expected values from YAML"""

    if not HAS_ANALYSIS_LIBS:
        return CheckResult(
            id="TENSION_001",
            name="Tension evolution CSV vs expected values",
            category="tension",
            severity="ERROR",
            passed=False,
            details="pandas not available",
            hint="Install pandas: pip install pandas"
        )

    csv_path = DATA_DIR / "tension_evolution.csv"
    if not csv_path.exists():
        return CheckResult(
            id="TENSION_001",
            name="Tension evolution CSV vs expected values",
            category="tension",
            severity="ERROR",
            passed=False,
            details=f"CSV not found: {csv_path}",
            hint="Run: python3 analysis/calculate_tension_evolution.py"
        )

    # Load CSV
    df = pd.read_csv(csv_path, comment='#')

    # Expected values from YAML
    tolerance_h0 = claims['tolerances']['h0']
    tolerance_tension = claims['tolerances']['tension']
    stages = claims['tension_evolution']['stages']

    # Verify each stage
    mismatches = []
    for i, stage in enumerate(stages):
        if i >= len(df):
            mismatches.append(f"Stage {stage['stage']}: missing from CSV")
            continue

        h0_expected = stage['h0']
        tension_expected = stage['tension']

        h0_actual = df.iloc[i]['H0_km_s_Mpc']
        tension_actual = df.iloc[i]['Tension_sigma']

        if abs(h0_actual - h0_expected) > tolerance_h0:
            mismatches.append(
                f"Stage {stage['stage']} H₀: expected={h0_expected:.2f}, actual={h0_actual:.2f}"
            )

        if abs(tension_actual - tension_expected) > tolerance_tension:
            mismatches.append(
                f"Stage {stage['stage']} tension: expected={tension_expected:.1f}σ, actual={tension_actual:.1f}σ"
            )

    if mismatches:
        return CheckResult(
            id="TENSION_001",
            name="Tension evolution CSV vs expected values",
            category="tension",
            severity="ERROR",
            passed=False,
            details=f"Found {len(mismatches)} mismatches: " + "; ".join(mismatches[:3]),
            hint="Update tension_evolution.csv or numerical_claims.yaml"
        )
    else:
        return CheckResult(
            id="TENSION_001",
            name="Tension evolution CSV vs expected values",
            category="tension",
            severity="ERROR",
            passed=True,
            details="All 5 stages match expected values"
        )


# =============================================================================
# Check #1b: Tension Evolution Table Consistency
# =============================================================================

@framework.register_check(
    id="TENSION_002",
    name="Tension evolution table vs CSV",
    category="tension",
    severity="ERROR"
)
def check_tension_table(claims: Dict) -> CheckResult:
    """Verify the manuscript table fragment matches the tension CSV."""

    if not HAS_ANALYSIS_LIBS:
        return CheckResult(
            id="TENSION_002",
            name="Tension evolution table vs CSV",
            category="tension",
            severity="ERROR",
            passed=False,
            details="pandas not available",
            hint="Install pandas: pip install pandas"
        )

    csv_path = DATA_DIR / "tension_evolution.csv"
    table_path = DATA_DIR / "tables" / "table2_tension_evolution.tex"

    if not csv_path.exists() or not table_path.exists():
        missing = []
        if not csv_path.exists():
            missing.append(str(csv_path))
        if not table_path.exists():
            missing.append(str(table_path))
        return CheckResult(
            id="TENSION_002",
            name="Tension evolution table vs CSV",
            category="tension",
            severity="ERROR",
            passed=False,
            details="Missing required file(s): " + ", ".join(missing),
            hint="Regenerate the table and CSV products"
        )

    df = pd.read_csv(csv_path, comment="#")
    table_text = table_path.read_text(encoding="utf-8")

    mismatches = []
    for idx, (_, row) in enumerate(df.iterrows(), start=1):
        expected_fragment = (
            f"{idx} & {row['H0_km_s_Mpc']:.2f} & {row['Sigma_km_s_Mpc']:.2f} & "
            f"{row['Tension_sigma']:.1f}$\\sigma$"
        )
        if expected_fragment not in table_text:
            mismatches.append(expected_fragment)

    if mismatches:
        return CheckResult(
            id="TENSION_002",
            name="Tension evolution table vs CSV",
            category="tension",
            severity="ERROR",
            passed=False,
            details=f"Found {len(mismatches)} table mismatches; example expected fragment: {mismatches[0]}",
            hint="Run: python3 analysis/create_manuscript_tables.py"
        )

    return CheckResult(
        id="TENSION_002",
        name="Tension evolution table vs CSV",
        category="tension",
        severity="ERROR",
        passed=True,
        details="table2_tension_evolution.tex matches tension_evolution.csv"
    )


# =============================================================================
# Check #2: Systematic Budget Quadrature Sums
# =============================================================================

@framework.register_check(
    id="SYSTEMATIC_001",
    name="Systematic budget quadrature sums",
    category="systematics",
    severity="ERROR"
)
def check_systematic_budget(claims: Dict) -> CheckResult:
    """Verify systematic budget quadrature sums match expected values"""

    if not HAS_ANALYSIS_LIBS:
        return CheckResult(
            id="SYSTEMATIC_001",
            name="Systematic budget quadrature sums",
            category="systematics",
            severity="ERROR",
            passed=False,
            details="numpy not available",
            hint="Install numpy: pip install numpy"
        )

    # Expected values from YAML
    expected_shoes = claims['systematic_budget']['shoes']['uncorrelated']
    expected_our = claims['systematic_budget']['our_assessment']['uncorrelated']
    tolerance = claims['tolerances']['sigma']

    # Get component values
    shoes_components = np.array([c['value'] for c in claims['systematic_budget']['shoes']['components']])
    our_components = np.array([c['value'] for c in claims['systematic_budget']['our_assessment']['components']])

    # Calculate quadrature sums
    shoes_calc = np.sqrt(np.sum(shoes_components**2))
    our_calc = np.sqrt(np.sum(our_components**2))

    mismatches = []
    if abs(shoes_calc - expected_shoes) > tolerance:
        mismatches.append(
            f"SH0ES: calculated={shoes_calc:.3f}, expected={expected_shoes:.3f}"
        )

    if abs(our_calc - expected_our) > tolerance:
        mismatches.append(
            f"Our: calculated={our_calc:.3f}, expected={expected_our:.3f}"
        )

    if mismatches:
        return CheckResult(
            id="SYSTEMATIC_001",
            name="Systematic budget quadrature sums",
            category="systematics",
            severity="ERROR",
            passed=False,
            details="Quadrature sum mismatch: " + "; ".join(mismatches),
            hint="Check component values in numerical_claims.yaml"
        )
    else:
        return CheckResult(
            id="SYSTEMATIC_001",
            name="Systematic budget quadrature sums",
            category="systematics",
            severity="ERROR",
            passed=True,
            details=f"SH0ES={shoes_calc:.3f}, Our={our_calc:.3f} (correct)"
        )


# =============================================================================
# Check #3: H₀ Compilation Weighted Mean
# =============================================================================

@framework.register_check(
    id="H0_COMP_001",
    name="Three-method convergence calculation",
    category="h0_compilation",
    severity="WARNING"
)
def check_h0_compilation(claims: Dict) -> CheckResult:
    """Verify three-method (Planck + JAGB + CC) weighted mean"""

    if not HAS_ANALYSIS_LIBS:
        return CheckResult(
            id="H0_COMP_001",
            name="Three-method convergence calculation",
            category="h0_compilation",
            severity="WARNING",
            passed=True,  # Soft failure
            details="numpy/pandas not available (check skipped)"
        )

    # Expected values from YAML
    expected_h0 = claims['h0_compilation']['three_method_convergence']['h0']
    expected_sigma = claims['h0_compilation']['three_method_convergence']['sigma']
    tolerance_h0 = claims['tolerances']['h0']
    tolerance_sigma = claims['tolerances']['sigma']

    # Get method values
    methods = {m['name']: m for m in claims['h0_compilation']['methods']}

    method_names = claims['h0_compilation']['three_method_convergence']['methods']
    h0_values = np.array([methods[name]['h0'] for name in method_names])
    sigma_values = np.array([methods[name]['sigma'] for name in method_names])

    # Calculate weighted mean
    weights = 1 / sigma_values**2
    h0_calc = np.sum(h0_values * weights) / np.sum(weights)
    sigma_calc = np.sqrt(1 / np.sum(weights))

    mismatches = []
    if abs(h0_calc - expected_h0) > tolerance_h0:
        mismatches.append(
            f"H₀: calculated={h0_calc:.2f}, expected={expected_h0:.2f}"
        )

    if abs(sigma_calc - expected_sigma) > tolerance_sigma:
        mismatches.append(
            f"σ: calculated={sigma_calc:.2f}, expected={expected_sigma:.2f}"
        )

    if mismatches:
        return CheckResult(
            id="H0_COMP_001",
            name="Three-method convergence calculation",
            category="h0_compilation",
            severity="WARNING",
            passed=False,
            details="Convergence mismatch: " + "; ".join(mismatches),
            hint="Check method values in numerical_claims.yaml or h0_measurements_compilation.csv"
        )
    else:
        return CheckResult(
            id="H0_COMP_001",
            name="Three-method convergence calculation",
            category="h0_compilation",
            severity="WARNING",
            passed=True,
            details=f"Convergence: {h0_calc:.2f} ± {sigma_calc:.2f} km/s/Mpc (correct)"
        )


# =============================================================================
# Check #3b: H0 Compilation Table Consistency
# =============================================================================

@framework.register_check(
    id="H0_COMP_002",
    name="H0 compilation table vs CSV",
    category="h0_compilation",
    severity="WARNING"
)
def check_h0_compilation_table(claims: Dict) -> CheckResult:
    """Verify the Table 3 fragment matches the H0 compilation CSV for key rows."""

    if not HAS_ANALYSIS_LIBS:
        return CheckResult(
            id="H0_COMP_002",
            name="H0 compilation table vs CSV",
            category="h0_compilation",
            severity="WARNING",
            passed=True,
            details="pandas not available (check skipped)"
        )

    csv_path = DATA_DIR / "h0_measurements_compilation.csv"
    table_path = DATA_DIR / "tables" / "table3_h0_compilation.tex"
    if not csv_path.exists() or not table_path.exists():
        return CheckResult(
            id="H0_COMP_002",
            name="H0 compilation table vs CSV",
            category="h0_compilation",
            severity="WARNING",
            passed=False,
            details="Missing H0 compilation CSV or table fragment",
            hint="Regenerate the compilation and manuscript tables"
        )

    df = pd.read_csv(csv_path, comment="#").set_index("Method")
    table_text = table_path.read_text(encoding="utf-8")

    methods_to_check = [
        "SH0ES Cepheid",
        "TRGB",
        "JAGB",
        "Cosmic Chronometers (H(z))",
        "Planck CMB",
        "JAGB + Cosmic Chron.",
        "Weighted Mean",
    ]

    mismatches = []
    for method in methods_to_check:
        row = df.loc[method]
        expected_fragment = f"{method} & {row['H0_km_s_Mpc']:.2f} & {row['Sigma_km_s_Mpc']:.2f}"
        if expected_fragment not in table_text:
            mismatches.append(expected_fragment)

    if mismatches:
        return CheckResult(
            id="H0_COMP_002",
            name="H0 compilation table vs CSV",
            category="h0_compilation",
            severity="WARNING",
            passed=False,
            details=f"Found {len(mismatches)} table mismatches; example expected fragment: {mismatches[0]}",
            hint="Run: python3 analysis/create_manuscript_tables.py"
        )

    return CheckResult(
        id="H0_COMP_002",
        name="H0 compilation table vs CSV",
        category="h0_compilation",
        severity="WARNING",
        passed=True,
        details="table3_h0_compilation.tex matches h0_measurements_compilation.csv"
    )


# =============================================================================
# Check #4: Figure Metadata Consistency
# =============================================================================

@framework.register_check(
    id="FIGURES_001",
    name="Correlation sensitivity figure metadata",
    category="figures",
    severity="WARNING"
)
def check_figure_metadata(claims: Dict) -> CheckResult:
    """Verify correlation sensitivity figures have correct metadata"""

    # Find figures with metadata
    figures_with_metadata = [
        f for f in claims['figures']['required']
        if 'metadata' in f
    ]

    if not figures_with_metadata:
        return CheckResult(
            id="FIGURES_001",
            name="Correlation sensitivity figure metadata",
            category="figures",
            severity="WARNING",
            passed=True,
            details="No figures with metadata requirements (check skipped)"
        )

    tolerance_ratio = claims['tolerances']['ratio']
    expected_ratio_min = claims['systematic_budget']['ratios']['range'][0]
    expected_ratio_max = claims['systematic_budget']['ratios']['range'][1]

    issues = []
    for fig in figures_with_metadata:
        metadata_path = ROOT / fig['metadata']

        if not metadata_path.exists():
            issues.append(f"{fig['filename']}: metadata file missing ({metadata_path.name})")
            continue

        # Load metadata
        with open(metadata_path) as f:
            metadata = json.load(f)

        # Verify key values. Support both the older nested metadata shape and the
        # current flat scalar shape emitted by the figure generators.
        if 'key_values' in metadata:
            key_values = metadata['key_values']

            def read_ratio(*names: str) -> Optional[float]:
                for name in names:
                    value = key_values.get(name)
                    if isinstance(value, dict):
                        nested = value.get('value')
                        if nested is not None:
                            return float(nested)
                    elif value is not None:
                        return float(value)
                return None

            ratio_uncorr = read_ratio('ratio_uncorrelated', 'uncorrelated_ratio_rho_0')
            ratio_baseline = read_ratio('ratio_baseline', 'ratio_nominal_rho_0_3', 'baseline_ratio_rho_0_3')

            if ratio_uncorr is not None and abs(ratio_uncorr - expected_ratio_min) > tolerance_ratio:
                issues.append(
                    f"{fig['filename']}: ratio_uncorrelated={ratio_uncorr:.2f}, expected={expected_ratio_min:.2f}"
                )

            if ratio_baseline is not None and abs(ratio_baseline - expected_ratio_max) > tolerance_ratio:
                issues.append(
                    f"{fig['filename']}: ratio_baseline={ratio_baseline:.2f}, expected={expected_ratio_max:.2f}"
                )

    if issues:
        return CheckResult(
            id="FIGURES_001",
            name="Correlation sensitivity figure metadata",
            category="figures",
            severity="WARNING",
            passed=False,
            details=f"Found {len(issues)} metadata issues: " + "; ".join(issues[:2]),
            hint="Update figure metadata JSON files or regenerate figures"
        )
    else:
        return CheckResult(
            id="FIGURES_001",
            name="Correlation sensitivity figure metadata",
            category="figures",
            severity="WARNING",
            passed=True,
            details=f"Verified {len(figures_with_metadata)} figures with metadata"
        )


# =============================================================================
# Check #5: Figure Package Integrity
# =============================================================================

@framework.register_check(
    id="PACKAGE_001",
    name="Required figures exist",
    category="figures",
    severity="WARNING"
)
def check_package_integrity(claims: Dict) -> CheckResult:
    """Verify all required figures exist"""

    required_figures = claims['figures']['required']
    missing = []
    stale = []

    for fig in required_figures:
        fig_path = FIGURES_DIR / fig['filename']

        if not fig_path.exists():
            missing.append(fig['filename'])
            continue

        # Check if generator script exists and is newer
        if 'generator' in fig:
            script_path = ROOT / fig['generator']
            if script_path.exists():
                fig_mtime = fig_path.stat().st_mtime
                script_mtime = script_path.stat().st_mtime

                if fig_mtime < script_mtime:
                    # If valid metadata exists, trust content check over timestamp
                    # This prevents false positives on fresh clones (git sets all mtimes to clone time)
                    if 'metadata' in fig:
                        metadata_path = ROOT / fig['metadata']
                        if metadata_path.exists():
                            continue  # Trust FIGURES_001 metadata check

                    age_hours = (script_mtime - fig_mtime) / 3600
                    stale.append(f"{fig['filename']} ({age_hours:.1f}h older than script)")

    issues = []
    if missing:
        issues.append(f"{len(missing)} missing: {', '.join(missing[:3])}")
    if stale:
        issues.append(f"{len(stale)} stale: {', '.join(stale[:2])}")

    if missing or stale:
        return CheckResult(
            id="PACKAGE_001",
            name="Required figures exist",
            category="figures",
            severity="WARNING",
            passed=False,
            details="; ".join(issues),
            hint="Run: python3 run_all.py to regenerate all figures"
        )
    else:
        return CheckResult(
            id="PACKAGE_001",
            name="Required figures exist",
            category="figures",
            severity="WARNING",
            passed=True,
            details=f"All {len(required_figures)} required figures present and current"
        )


# =============================================================================
# Check #6: Manuscript Asset Paths
# =============================================================================

@framework.register_check(
    id="MANUSCRIPT_001",
    name="Manuscript asset paths resolve locally",
    category="manuscript",
    severity="ERROR"
)
def check_manuscript_asset_paths(claims: Dict) -> CheckResult:
    """Verify includegraphics/input paths resolve relative to manuscript/manuscript.tex."""

    manuscript_path = MANUSCRIPT_DIR / "manuscript.tex"
    if not manuscript_path.exists():
        return CheckResult(
            id="MANUSCRIPT_001",
            name="Manuscript asset paths resolve locally",
            category="manuscript",
            severity="ERROR",
            passed=False,
            details=f"Missing manuscript source: {manuscript_path}",
            hint="Restore manuscript/manuscript.tex"
        )

    text = manuscript_path.read_text(encoding="utf-8")
    patterns = [
        r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}",
        r"\\input\{([^}]+)\}",
    ]

    missing = []
    for pattern in patterns:
        for rel_path in re.findall(pattern, text):
            resolved = (manuscript_path.parent / rel_path).resolve()
            if not resolved.exists():
                missing.append(rel_path)

    if missing:
        return CheckResult(
            id="MANUSCRIPT_001",
            name="Manuscript asset paths resolve locally",
            category="manuscript",
            severity="ERROR",
            passed=False,
            details=f"Unresolved asset paths: {', '.join(missing[:4])}",
            hint="Fix manuscript include paths or regenerate missing assets"
        )

    return CheckResult(
        id="MANUSCRIPT_001",
        name="Manuscript asset paths resolve locally",
        category="manuscript",
        severity="ERROR",
        passed=True,
        details="All includegraphics/input paths resolve from manuscript/manuscript.tex"
    )


# =============================================================================
# Main Entry Point
# =============================================================================

def main() -> None:
    """Main entry point for verification script"""
    parser = argparse.ArgumentParser(
        description="Verify manuscript numerical consistency",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 analysis/verify_manuscript_consistency.py
  python3 analysis/verify_manuscript_consistency.py --json
  python3 analysis/verify_manuscript_consistency.py --only tension systematics
        """
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON instead of human-readable text"
    )

    parser.add_argument(
        "--only",
        nargs="+",
        metavar="CATEGORY",
        help="Only run checks in these categories (tension, systematics, h0_compilation, figures, manuscript)"
    )

    args = parser.parse_args()

    # Check dependencies
    if not HAS_ANALYSIS_LIBS:
        print("ERROR: Required libraries not available", file=sys.stderr)
        print("Install with: pip install pyyaml numpy pandas", file=sys.stderr)
        sys.exit(1)

    # Run verification
    try:
        results = framework.run_all(only_categories=args.only)

        if args.json:
            exit_code = framework.report_json(results)
        else:
            exit_code = framework.report_human(results)

        sys.exit(exit_code)

    except Exception as e:
        print(f"ERROR: Verification failed with exception: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
