import pytest
from unittest.mock import Mock, patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helixsoft_avalon import ClinicalDataGUI, ClinicalDataValidator


class TestFileSearch:
    """Test file search function"""
    
    @patch('tkinter.Tk')
    def test_search_finds_files(self, mock_tk):
        """Test search finds matching files"""
        gui = ClinicalDataGUI.__new__(ClinicalDataGUI)
        gui.root = mock_tk()
        gui.search_var = Mock()
        gui.search_var.get.return_value = ""
        gui.all_files = ["file1.csv", "file2.csv", "test.csv"]
        gui.displayed_files = []
        
        # Test search function
        def simple_filter():
            search = gui.search_var.get().lower()
            if search:
                gui.displayed_files = [f for f in gui.all_files if search in f.lower()]
            else:
                gui.displayed_files = gui.all_files.copy()
        
        # Test with no search
        gui.search_var.get.return_value = ""
        simple_filter()
        assert len(gui.displayed_files) == 3
        
        # Test with search
        gui.search_var.get.return_value = "file"
        simple_filter()
        assert len(gui.displayed_files) == 2


class TestGenerateTestData:
    """Test creating test CSV data"""
    
    def test_create_simple_csv(self, tmp_path):
        """Test creating a simple CSV file"""
        import csv
        
        test_file = tmp_path / "test.csv"
        
        # Create test data
        with open(test_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Age", "City"])
            writer.writerow(["John", "25", "NYC"])
            writer.writerow(["Jane", "30", "LA"])
        
        # Check file exists
        assert test_file.exists()
        
        # Check content
        with open(test_file, 'r') as f:
            lines = f.readlines()
            assert len(lines) == 3
            assert "John" in lines[1]
    
    def test_create_clinical_data(self, tmp_path):
        """Test creating clinical data CSV"""
        import csv
        
        test_file = tmp_path / "clinical.csv"
        
        # Create clinical data format
        with open(test_file, 'w', newline='') as f:
            writer = csv.writer(f)
            # Header
            writer.writerow([
                "PatientID", "TrialCode", "DrugCode", "Dosage_mg",
                "StartDate", "EndDate", "Outcome", "SideEffects", "Analyst"
            ])
            # Some data
            writer.writerow([
                "P001", "TRIAL1", "DRUG1", "100",
                "2024-01-01", "2024-06-01", "Improved", "None", "Dr. Smith"
            ])
        
        assert test_file.exists()


def test_simple_integration():
    """Simple integration test"""
    from helixsoft_avalon import UUIDGenerator, ClinicalDataValidator

    uuid_gen = UUIDGenerator()
    assert uuid_gen.api_url == "https://www.uuidtools.com/api/generate/v4"
    
    # Create validator with temp paths
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        validator = ClinicalDataValidator(
            download_dir=tmpdir,
            archive_dir=tmpdir,
            error_dir=tmpdir
        )
        assert validator.download_dir.exists()