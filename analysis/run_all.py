#!/usr/bin/env python3
"""
Master Script: Regenerate All Figures and Verify Data Integrity

Runs all figure generation scripts in sequence to ensure complete
reproducibility of manuscript figures from raw data.

Usage:
    python3 analysis/run_all.py              # Generate all figures
    python3 analysis/run_all.py --verify     # Also verify data integrity
    python3 analysis/run_all.py --figures-only  # Skip data verification

Output:
    - All manuscript figures regenerated in figures/
    - Summary report of generated files
    - Optional data integrity checks
"""
import sys
import subprocess
import time
from pathlib import Path
import argparse
import yaml

PYTHON = sys.executable

# Load figure scripts and expected outputs from YAML contract
# This eliminates the "shadow config" and ensures single source of truth
def load_targets_from_contract():
    """Load figure generation scripts and expected outputs from numerical_claims.yaml"""
    config_path = Path(__file__).parent.parent / 'config' / 'numerical_claims.yaml'

    with open(config_path) as f:
        data = yaml.safe_load(f)

    scripts = []
    expected_outputs = []

    for fig in data['figures']['required']:
        # Add generator script (avoid duplicates if multiple figures from one script)
        if 'generator' in fig:
            if fig['generator'] not in scripts:
                scripts.append(fig['generator'])

        # Add expected output file (both PNG and PDF if applicable)
        filename = fig['filename']
        expected_outputs.append(f"figures/{filename}")

        # If it's a PDF, also expect PNG version
        if filename.endswith('.pdf'):
            expected_outputs.append(f"figures/{filename.replace('.pdf', '.png')}")

    return scripts, expected_outputs

# Dynamically load from YAML contract
FIGURE_SCRIPTS, EXPECTED_OUTPUTS = load_targets_from_contract()

# Critical data files (for integrity verification)
CRITICAL_DATA_FILES = [
    'data/tension_evolution.csv',
    'data/h0_measurements_compilation.csv',
    'data/correlation_matrix_updated.csv',
]


def run_script(script_path, verbose=True):
    """Run a single Python script and capture output"""
    if verbose:
        print(f"\n{'='*70}")
        print(f"Running: {script_path}")
        print(f"{'='*70}")

    start_time = time.time()

    try:
        result = subprocess.run(
            [PYTHON, script_path],
            capture_output=True,
            text=True,
            check=True,
            timeout=60  # 60 second timeout per script
        )

        elapsed = time.time() - start_time

        if verbose:
            print(result.stdout)

        return {
            'success': True,
            'elapsed': elapsed,
            'stdout': result.stdout,
            'stderr': result.stderr
        }

    except subprocess.CalledProcessError as e:
        elapsed = time.time() - start_time
        print(f"❌ ERROR running {script_path}:")
        print(e.stderr)
        return {
            'success': False,
            'elapsed': elapsed,
            'error': str(e),
            'stderr': e.stderr
        }
    except subprocess.TimeoutExpired:
        print(f"⏱️  TIMEOUT: {script_path} exceeded 60 seconds")
        return {
            'success': False,
            'elapsed': 60.0,
            'error': 'Timeout after 60 seconds'
        }


def verify_outputs(expected_files):
    """Verify that all expected output files exist"""
    missing = []
    present = []

    for filepath in expected_files:
        path = Path(filepath)
        if path.exists():
            size_kb = path.stat().st_size / 1024
            present.append((filepath, size_kb))
        else:
            missing.append(filepath)

    return present, missing


def verify_data_integrity(data_files):
    """Check that critical data files exist and are readable"""
    issues = []

    for filepath in data_files:
        path = Path(filepath)
        if not path.exists():
            issues.append(f"Missing: {filepath}")
        else:
            try:
                with open(path, 'r') as f:
                    lines = f.readlines()
                    if len(lines) == 0:
                        issues.append(f"Empty: {filepath}")
            except Exception as e:
                issues.append(f"Unreadable {filepath}: {e}")

    return issues


def print_summary(results, present_files, missing_files, elapsed_total):
    """Print comprehensive summary report"""
    print("\n" + "="*70)
    print("EXECUTION SUMMARY")
    print("="*70)

    successful = sum(1 for r in results if r['success'])
    failed = len(results) - successful

    print(f"\n📊 Scripts Executed: {len(results)}")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   ⏱️  Total time: {elapsed_total:.2f} seconds")

    if failed > 0:
        print("\n❌ Failed Scripts:")
        for i, result in enumerate(results):
            if not result['success']:
                print(f"   • {FIGURE_SCRIPTS[i]}")
                if 'error' in result:
                    print(f"     Error: {result['error']}")

    print(f"\n📁 Generated Files: {len(present_files)}")
    for filepath, size_kb in present_files:
        print(f"   ✅ {filepath} ({size_kb:.1f} KB)")

    if missing_files:
        print(f"\n⚠️  Missing Expected Files: {len(missing_files)}")
        for filepath in missing_files:
            print(f"   ❌ {filepath}")

    print("\n" + "="*70)

    if failed == 0 and len(missing_files) == 0:
        print("✨ SUCCESS: All figures generated successfully!")
    else:
        print("⚠️  WARNING: Some issues detected. Review output above.")

    print("="*70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Regenerate all manuscript figures'
    )
    parser.add_argument('--verify', action='store_true',
                       help='Verify data integrity before running')
    parser.add_argument('--figures-only', action='store_true',
                       help='Skip data verification')
    parser.add_argument('--quiet', action='store_true',
                       help='Minimal output (errors only)')

    args = parser.parse_args()

    verbose = not args.quiet

    if verbose:
        print("="*70)
        print("MANUSCRIPT FIGURE REGENERATION")
        print("Distance Ladder Systematics Analysis")
        print("="*70)

    # Optional: Verify data integrity first
    if args.verify and not args.figures_only:
        if verbose:
            print("\n🔍 Verifying data integrity...")
        issues = verify_data_integrity(CRITICAL_DATA_FILES)
        if issues:
            print("❌ Data integrity issues found:")
            for issue in issues:
                print(f"   • {issue}")
            print("\nAborting: Fix data issues before regenerating figures.")
            sys.exit(1)
        if verbose:
            print("✅ All critical data files present and readable")

    # Run all figure generation scripts
    start_time = time.time()
    results = []

    for script in FIGURE_SCRIPTS:
        result = run_script(script, verbose=verbose)
        results.append(result)

        # Stop on first error if requested
        if not result['success'] and not args.quiet:
            print(f"\n⚠️  Script {script} failed. Continuing with remaining scripts...")

    elapsed_total = time.time() - start_time

    # Verify outputs
    present_files, missing_files = verify_outputs(EXPECTED_OUTPUTS)

    # Print summary
    print_summary(results, present_files, missing_files, elapsed_total)

    # Run manuscript verification
    if not args.figures_only:
        if verbose:
            print("\n" + "="*70)
            print("RUNNING MANUSCRIPT VERIFICATION")
            print("="*70 + "\n")

        try:
            verify_result = subprocess.run(
                [PYTHON, 'analysis/verify_manuscript_consistency.py'],
                capture_output=True,
                text=True,
                timeout=10
            )

            if verbose:
                print(verify_result.stdout)

            # Check verification exit code
            if verify_result.returncode != 0:
                print("\n⚠️  Note: Manuscript verification reported issues.")
                print("   Run manually for details: python3 analysis/verify_manuscript_consistency.py")
                print()
            else:
                if verbose:
                    print("\n✅ Manuscript verification passed!")
                    print()

        except subprocess.TimeoutExpired:
            print("\n⚠️  Verification timeout (skipping)")
        except FileNotFoundError:
            print("\n⚠️  Verification script not found (skipping)")
        except Exception as e:
            print(f"\n⚠️  Verification failed: {e}")

    # Exit with error code if any failures
    if any(not r['success'] for r in results) or missing_files:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
