import unittest
import os
import pandas as pd
import json
from unittest.mock import patch

class TestEmployeeDataScraper(unittest.TestCase):
    
    def setUp(self):
        self.filename = "employees.json"

    def test_01_json_file_exists(self):
        """Test Case 1: Check if JSON file exists."""
        print("employees.json exists:", os.path.isfile("employees.json"))  #should return True

    def test_02_json_file_extraction(self):
        """Test Case 2: Verify JSON file extraction."""
        try:
            df = pd.read_json(self.filename)
            print("\nFirst 5 rows of the dataset:\n", df.head())  
            self.assertIsInstance(df, pd.DataFrame)
        except Exception as e:
            self.fail(f"JSON extraction failed: {e}")

    def test_03_file_extension(self):
        """Test Case 3: Verify file type and data type."""
        df = pd.read_json("employees.json")
        print("File extension:", os.path.splitext("employees.json")[1])  #should return '.json'
        print("Age data type is", df["age"].dtype)  #should be 'INT'

    def test_04_validate_data_structure(self):
        """Test Case 4: Validate Data Structure."""
        expected_keys = [
            "id", "first_name", "last_name", "email", "phone",
            "gender", "age", "job_title",
            "years_of_experience", "salary", "department"
        ]
        df = pd.read_json(self.filename)
        print(df.columns.tolist() == expected_keys)  #should return True

    def test_05_no_missing_values(self):
        """Test Case 5: Handle Missing or Invalid Data."""
        df = pd.read_json(self.filename)
        print(df.isnull().sum().to_string())  #should show zero missing values    

if __name__ == "__main__":
    unittest.main()