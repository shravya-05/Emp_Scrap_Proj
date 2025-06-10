import requests
import json
import logging
import random

API_URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

#predefined hire dates for variation
hire_dates = ["2018-05-10", "2019-09-15", "2020-07-20", "2021-12-01", "2022-04-30"]

def fetch_employee_data():
    """fetch employee data and assign predefined hire dates."""
    try:
        logging.info("Fetching employee data...")
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()  #raise error for non-200 status codes
        data = response.json()

        if isinstance(data, list):
            #sssign a random predefined "Hire Date" to each employee
            for employee in data:
                employee.setdefault("Hire Date", random.choice(hire_dates))  

            #now save modified data to JSON file
            with open("employees.json", "w") as f:
                json.dump(data, f, indent=4)

            logging.info(f"Data saved successfully: {len(data)} employees stored in 'employee.json'")
            

        else:
            logging.error("Unexpected data format: Expected a list.")

    except requests.exceptions.Timeout:
        logging.error("Request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")

if __name__ == "__main__":
    fetch_employee_data()
