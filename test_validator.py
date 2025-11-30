import pytest
from helixsoft_avalon import ClinicalDataValidator


class TestClinicalDataValidator:
    def test_multiple_filename_patterns(self):
        """REFACTOR: Test various filename patterns"""
        validator = ClinicalDataValidator("/tmp", "/tmp", "/tmp")

        # Test valid patterns
        valid_files = [
            "CLINICALDATA20251111083303.csv",
            "CLINICALDATA20250101000000.CSV"
        ]

        # Test invalid patterns
        invalid_files = [
            "wrong_name.csv",
            "DATA20251111083303.csv",
            "CLINICALDATA20251111.csv"  # too short
        ]

        for file in valid_files:
            assert validator._validate_filename_pattern(file) == True

        for file in invalid_files:
            assert validator._validate_filename_pattern(file) == False
