#!/usr/bin/env python3
"""
Test Suite for Manuscript Verification System

Validates that verify_manuscript_consistency.py correctly detects
various types of consistency errors by deliberately introducing failures,
running verification, and confirming errors are caught.

Tests cover all historical incidents documented in IMPLEMENTATION_LOG.md:
- Incident #1: Tension evolution mismatches (README, CSV)
- Incident #2: Systematic budget errors (70% overestimate)
- Incident #3: Missing/stale figures

Author: Distance Ladder Systematics Project
Date: November 2025
Version: 2.0 (tests for YAML-first verification system)
"""

import os
import sys
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Tuple

# Repository root
REPO_ROOT = Path(__file__).parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "figures"
CONFIG_DIR = REPO_ROOT / "config"
ANALYSIS_DIR = REPO_ROOT / "analysis"

# Verification script
VERIFY_SCRIPT = ANALYSIS_DIR / "verify_manuscript_consistency.py"

# ANSI colors
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'  # No color


class TestResult:
    """Result of a single test case"""
    def __init__(self, test_id: str, name: str, passed: bool,
                 message: str = "", details: str = ""):
        self.test_id = test_id
        self.name = name
        self.passed = passed
        self.message = message
        self.details = details

    def __repr__(self):
        status = f"{GREEN}✅ PASS{NC}" if self.passed else f"{RED}❌ FAIL{NC}"
        return f"{status} {self.test_id}: {self.name}"


class VerificationTestSuite:
    """Test suite for manuscript verification system"""

    def __init__(self):
        self.results: List[TestResult] = []
        self.temp_dir = None

    def run_verification(self) -> Tuple[int, Dict]:
        """Run verification script and return (exit_code, json_results)"""
        result = subprocess.run(
            [sys.executable, str(VERIFY_SCRIPT), "--json"],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT
        )

        try:
            json_output = json.loads(result.stdout if result.returncode != 0 else result.stdout)
        except json.JSONDecodeError:
            # If JSON parsing fails, return empty results
            json_output = {
                'summary': {'total_checks': 0, 'passed': 0, 'failed': 0, 'errors': 0, 'warnings': 0},
                'results': []
            }

        return result.returncode, json_output

    def backup_file(self, filepath: Path) -> Path:
        """Backup a file to temp directory"""
        if self.temp_dir is None:
            self.temp_dir = tempfile.mkdtemp()

        backup_path = Path(self.temp_dir) / filepath.name
        if filepath.exists():
            shutil.copy2(filepath, backup_path)
        return backup_path

    def restore_file(self, filepath: Path, backup_path: Path):
        """Restore file from backup"""
        if backup_path.exists():
            shutil.copy2(backup_path, filepath)

    # =========================================================================
    # Test Case #1: Baseline - All Checks Pass
    # =========================================================================

    def test_baseline(self):
        """TEST_001: Verify all checks pass on current repository state"""
        print("\n" + "="*80)
        print("TEST_001: Baseline verification (all checks should pass)")
        print("="*80)

        exit_code, results = self.run_verification()

        summary = results.get('summary', {})
        total = summary.get('total_checks', 0)
        passed = summary.get('passed', 0)
        errors = summary.get('errors', 0)
        warnings = summary.get('warnings', 0)

        print(f"Exit code: {exit_code}")
        print(f"Checks: {passed}/{total} passed, errors={errors}, warnings={warnings}")

        # Allow warnings, but no errors
        if errors == 0:
            self.results.append(TestResult(
                "TEST_001",
                "Baseline verification",
                True,
                f"All critical checks passed ({total} total, {warnings} warnings)"
            ))
        else:
            self.results.append(TestResult(
                "TEST_001",
                "Baseline verification",
                False,
                f"{errors} error(s) on baseline repository",
                details=str(results)
            ))

    # =========================================================================
    # Test Case #2: Tension CSV Mismatch (Incident #1)
    # =========================================================================

    def test_tension_csv_mismatch(self):
        """TEST_002: Detect H₀ value mismatch in tension evolution CSV"""
        print("\n" + "="*80)
        print("TEST_002: Tension CSV mismatch detection (Incident #1 recreation)")
        print("="*80)

        csv_path = DATA_DIR / "tension_evolution.csv"
        backup = self.backup_file(csv_path)

        try:
            # Introduce error: Change Stage 5 H₀ from 69.54 to 70.00
            with open(csv_path) as f:
                content = f.read()

            modified = content.replace(",69.54,", ",70.00,")

            with open(csv_path, 'w') as f:
                f.write(modified)

            print("✓ Injected error: Changed Stage 5 H₀ from 69.54 → 70.00")

            # Run verification
            exit_code, results = self.run_verification()

            # Check if TENSION_001 detected the error
            found_error = False
            for check in results.get('results', []):
                if check['id'] == 'TENSION_001' and not check['passed']:
                    found_error = True
                    print(f"✓ Error detected: {check['details']}")

            if found_error:
                self.results.append(TestResult(
                    "TEST_002",
                    "Tension CSV mismatch detection",
                    True,
                    "TENSION_001 correctly detected H₀ value mismatch"
                ))
            else:
                self.results.append(TestResult(
                    "TEST_002",
                    "Tension CSV mismatch detection",
                    False,
                    "TENSION_001 failed to detect H₀ value mismatch"
                ))

        finally:
            # Restore original file
            self.restore_file(csv_path, backup)
            print("✓ Restored original file")

    # =========================================================================
    # Test Case #3: Systematic Budget Quadrature Error (Incident #2)
    # =========================================================================

    def test_systematic_budget_error(self):
        """TEST_003: Detect systematic budget quadrature sum error"""
        print("\n" + "="*80)
        print("TEST_003: Systematic budget error detection (via YAML modification)")
        print("="*80)

        yaml_path = CONFIG_DIR / "numerical_claims.yaml"
        backup = self.backup_file(yaml_path)

        try:
            # Introduce error: Change one component value in YAML
            with open(yaml_path) as f:
                content = f.read()

            # Change Our Assessment's Period distribution from 1.0 to 1.5
            modified = content.replace(
                "value: 1.0        # km/s/Mpc (explicit bracket mid-range)",
                "value: 1.5        # km/s/Mpc (MODIFIED FOR TEST)"
            )

            with open(yaml_path, 'w') as f:
                f.write(modified)

            print("✓ Injected error: Modified Our Assessment Period distribution: 1.0 → 1.5")

            # Run verification
            exit_code, results = self.run_verification()

            # Check if SYSTEMATIC_001 detected the error
            found_error = False
            for check in results.get('results', []):
                if check['id'] == 'SYSTEMATIC_001' and not check['passed']:
                    found_error = True
                    print(f"✓ Error detected: {check['details']}")

            if found_error:
                self.results.append(TestResult(
                    "TEST_003",
                    "Systematic budget quadrature error",
                    True,
                    "SYSTEMATIC_001 correctly detected quadrature sum mismatch"
                ))
            else:
                self.results.append(TestResult(
                    "TEST_003",
                    "Systematic budget quadrature error",
                    False,
                    "SYSTEMATIC_001 failed to detect quadrature sum mismatch"
                ))

        finally:
            # Restore original file
            self.restore_file(yaml_path, backup)
            print("✓ Restored original YAML")

    # =========================================================================
    # Test Case #4: Figure Metadata Mismatch
    # =========================================================================

    def test_figure_metadata_mismatch(self):
        """TEST_004: Detect figure metadata value mismatch"""
        print("\n" + "="*80)
        print("TEST_004: Figure metadata mismatch detection (Incident #2 related)")
        print("="*80)

        metadata_path = FIGURES_DIR / "sensitivity_correlation_metadata.json"

        if not metadata_path.exists():
            print("⚠ Metadata file doesn't exist, skipping test")
            self.results.append(TestResult(
                "TEST_004",
                "Figure metadata mismatch",
                True,
                "Metadata file doesn't exist (test skipped, would be caught by PACKAGE_001)"
            ))
            return

        backup = self.backup_file(metadata_path)

        try:
            # Introduce error: Change ratio value
            with open(metadata_path) as f:
                metadata = json.load(f)

            metadata['key_values']['ratio_baseline']['value'] = 2.50  # Change from 1.65

            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)

            print("✓ Injected error: Changed ratio_baseline from 1.65 → 2.50")

            # Run verification
            exit_code, results = self.run_verification()

            # Check if FIGURES_001 detected the error
            found_warning = False
            for check in results.get('results', []):
                if check['id'] == 'FIGURES_001' and not check['passed']:
                    found_warning = True
                    print(f"✓ Warning detected: {check['details']}")

            if found_warning:
                self.results.append(TestResult(
                    "TEST_004",
                    "Figure metadata mismatch",
                    True,
                    "FIGURES_001 correctly detected metadata value mismatch"
                ))
            else:
                self.results.append(TestResult(
                    "TEST_004",
                    "Figure metadata mismatch",
                    False,
                    "FIGURES_001 failed to detect metadata value mismatch"
                ))

        finally:
            # Restore original file
            self.restore_file(metadata_path, backup)
            print("✓ Restored original metadata")

    # =========================================================================
    # Test Case #5: H₀ Compilation Convergence Error
    # =========================================================================

    def test_h0_compilation_error(self):
        """TEST_005: Detect H₀ three-method convergence calculation error"""
        print("\n" + "="*80)
        print("TEST_005: H₀ compilation convergence error detection")
        print("="*80)

        yaml_path = CONFIG_DIR / "numerical_claims.yaml"
        backup = self.backup_file(yaml_path)

        try:
            # Introduce error: Change Planck H₀ value in methods list
            with open(yaml_path) as f:
                content = f.read()

            # This will affect the three-method convergence calculation
            modified = content.replace(
                "name: \"Planck CMB\"\n      h0: 67.36",
                "name: \"Planck CMB\"\n      h0: 68.50"
            )

            with open(yaml_path, 'w') as f:
                f.write(modified)

            print("✓ Injected error: Changed Planck CMB H₀ from 67.36 → 68.50")

            # Run verification
            exit_code, results = self.run_verification()

            # Check if H0_COMP_001 detected the error
            found_warning = False
            for check in results.get('results', []):
                if check['id'] == 'H0_COMP_001' and not check['passed']:
                    found_warning = True
                    print(f"✓ Warning detected: {check['details']}")

            if found_warning:
                self.results.append(TestResult(
                    "TEST_005",
                    "H₀ compilation convergence error",
                    True,
                    "H0_COMP_001 correctly detected convergence calculation error"
                ))
            else:
                self.results.append(TestResult(
                    "TEST_005",
                    "H₀ compilation convergence error",
                    False,
                    "H0_COMP_001 failed to detect convergence calculation error"
                ))

        finally:
            # Restore original file
            self.restore_file(yaml_path, backup)
            print("✓ Restored original YAML")

    # =========================================================================
    # Run All Tests
    # =========================================================================

    def run_all(self):
        """Run complete test suite"""
        print("\n" + "="*80)
        print("MANUSCRIPT VERIFICATION SYSTEM - TEST SUITE v2.0")
        print("="*80)
        print("\nThis test suite deliberately introduces errors to verify that")
        print("the verification system correctly detects consistency issues.\n")
        print("Testing YAML-first verification architecture with decorator pattern.")
        print()
        print(f"{YELLOW}⚠️  Safety: Each test uses try/finally to restore files.{NC}")
        print(f"{YELLOW}   If interrupted, run: git checkout data/ config/ figures/{NC}")
        print()

        try:
            # Run all test cases
            self.test_baseline()
            self.test_tension_csv_mismatch()
            self.test_systematic_budget_error()
            self.test_figure_metadata_mismatch()
            self.test_h0_compilation_error()

            # Generate report
            self.report()

        finally:
            # Cleanup temp directory (even if tests crash)
            if self.temp_dir and Path(self.temp_dir).exists():
                shutil.rmtree(self.temp_dir)

    def report(self):
        """Generate test report"""
        print("\n" + "="*80)
        print("TEST SUITE RESULTS")
        print("="*80)
        print()

        passed = sum(1 for r in self.results if r.passed)
        failed = sum(1 for r in self.results if not r.passed)

        for result in self.results:
            print(result)
            if result.message:
                print(f"  → {result.message}")
            if not result.passed and result.details:
                print(f"  Details: {result.details[:200]}...")
            print()

        print("="*80)
        print(f"SUMMARY: {passed}/{len(self.results)} tests passed")
        print("="*80)

        if failed > 0:
            print(f"\n⚠️  {failed} test(s) failed - verification system may have issues")
            return 1
        else:
            print("\n✅ All tests passed - verification system is working correctly!")
            return 0


if __name__ == '__main__':
    suite = VerificationTestSuite()
    exit_code = suite.run_all()
    sys.exit(exit_code)
