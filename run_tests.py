
import subprocess
import sys
import os

def run_pytest(test_dir, test_file=None):
    """Run pytest in specified directory"""
    cmd = [sys.executable, "-m", "pytest"]
    
    if test_file:
        cmd.append(test_file)
    else:
        cmd.append(test_dir)
    
    cmd.extend(["-v", "--tb=short"])
    
    print(f"\n{'='*60}")
    print(f"Running tests in: {test_dir}")
    print(f"{'='*60}")
    
    result = subprocess.run(cmd)
    return result.returncode

def main():
    """Run all test suites"""
    print("Running Test Suites for Clinical Data Processor")
    print("="*60)
    
    # Run UUID API integration tests
    uuid_tests_passed = run_pytest("uuid_api_integration") == 0
    
    # Run unit tests
    unit_tests_passed = run_pytest("unit_test") == 0
    
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    print(f"UUID API Integration Tests: {'PASSED' if uuid_tests_passed else 'FAILED'}")
    print(f"Unit Tests: {'PASSED' if unit_tests_passed else 'FAILED'}")
    print(f"{'='*60}")
    
    if uuid_tests_passed and unit_tests_passed:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())