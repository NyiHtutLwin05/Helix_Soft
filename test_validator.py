from helixsoft_avalon import ClinicalDataValidator


def test_valid_filename_should_pass():
    """RED: This might fail if pattern is strict"""
    validator = ClinicalDataValidator("/tmp", "/tmp", "/tmp")

    result = validator._validate_filename_pattern(
        "CLINICALDATA20251111083303.csv")
    assert result == True  # ❌ FAILS because _validate_filename_pattern method returns False
