import unittest
import pandas as pd
import json

class TestDataNormalization(unittest.TestCase):
    """Unit tests for data normalization."""

    @classmethod
    def setUpClass(cls):
        """Load normalized data before running tests."""
        with open("employees.json", "r") as f:
            raw_data = json.load(f)
        cls.raw_df = pd.DataFrame(raw_data)

        cls.normalized_df = pd.read_csv("normalized_employees.csv")

    def test_full_name_exists(self):
        """Check if 'Full Name' column is created correctly."""
        self.assertIn("Full Name", self.normalized_df.columns)

    def test_designation_mapping(self):
        """Verify designation assignment based on experience."""
        if "years_of_experience" in self.raw_df.columns:
            for _, row in self.raw_df.iterrows():
                expected_designation = (
                    "System Engineer" if row["years_of_experience"] < 3 else
                    "Data Engineer" if 3 <= row["years_of_experience"] <= 5 else
                    "Senior Data Engineer" if 5 < row["years_of_experience"] <= 10 else
                    "Lead"
                )
                normalized_value = self.normalized_df.loc[self.normalized_df["email"] == row["email"], "Designation"].values
                if normalized_value:
                    self.assertEqual(normalized_value[0], expected_designation)

    def test_phone_validation(self):
        """Ensure phone numbers are correctly marked as 'Invalid Number' when containing 'x'."""
        if "phone" in self.raw_df.columns:
            for _, row in self.raw_df.iterrows():
                expected_phone = "Invalid Number" if "x" in str(row["phone"]) else str(row["phone"])
                normalized_value = self.normalized_df.loc[self.normalized_df["email"] == row["email"], "Phone"].values
                if normalized_value:
                    self.assertEqual(normalized_value[0], expected_phone)

    def test_hire_date_format(self):
        """Check if 'Hire Date' is formatted correctly."""
        if "Hire Date" in self.normalized_df.columns:
            for date in self.normalized_df["Hire Date"]:
                self.assertRegex(date, r"\d{4}-\d{2}-\d{2}")  #it matches YYYY-MM-DD format

if __name__ == "__main__":
    unittest.main()