import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import requests
import os
import scraper

class TestEmployeeScraper(unittest.TestCase):


    @patch("requests.get")
    def test_01_verify_json_file_download(self, mock_get):
        """Test if API returns a valid JSON response."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": [{"id": 1, "first_name": "John"}]}
        
        response = requests.get(scraper.API_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())

    @patch("requests.get")
    def test_02_verify_json_extraction(self, mock_get):
        """Test if data is extracted correctly from JSON."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": [{
                "id": 1,
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jane@example.com",
                "phone": "1234567890",
                "hire_date": "2022-05-20"
            }]
        }

        response = requests.get(scraper.API_URL)
        employee = response.json()["data"][0]

        self.assertIn("first_name", employee)
        self.assertIn("last_name", employee)
        self.assertIn("email", employee)
        self.assertIn("phone", employee)
        self.assertIn("hire_date", employee)

    def test_03_validate_file_format(self):
        """Test if file has correct JSON extension."""
        filename = "employees.json"
        extension = os.path.splitext(filename)[1]
        self.assertEqual(extension, ".json")

    def test_04_validate_data_structure(self):
        """Test employee schema and normalized fields."""
        sample = {
            "first_name": "Alan",
            "last_name": "Walker",
            "email": "alan@example.com",
            "phone": "1234567890",
            "gender": "Male",
            "age": 29,
            "job_title": "Developer",
            "years_of_experience": 6,
            "salary": 80000,
            "department": "IT",
            "hire_date": "2019-08-15"
        }

        df = pd.DataFrame([sample])
        normalized_df = scraper.normalize_employee_data(df.to_dict(orient="records"))
        row = normalized_df.iloc[0]

        self.assertEqual(row["Full Name"], "Alan Walker")
        self.assertEqual(row["designation"], "Senior Data Engineer")
        self.assertEqual(row["phone"], 1234567890)
        self.assertEqual(row["hire_date"], "2019-08-15")

    def test_05_handle_missing_or_invalid_data(self):
        """Test how missing or invalid fields are handled."""
        incomplete = {
            "first_name": "Tina",
            "phone": "1234x6789",
            "years_of_experience": 2
        }

        df = pd.DataFrame([incomplete])
        normalized_df = scraper.normalize_employee_data(df.to_dict(orient="records"))
        row = normalized_df.iloc[0]

        self.assertEqual(row["Full Name"].strip(), "Tina")
        self.assertEqual(row["designation"], "System Engineer")
        self.assertEqual(row["phone"], "Invalid Number")

    

   


if __name__ == '__main__':
    unittest.main()

