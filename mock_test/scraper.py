import requests
import pandas as pd
from datetime import datetime

API_URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"

# Designation logic
def get_designation(years):
    try:
        y = int(years)
        if y < 3:
            return "System Engineer"
        elif y <= 5:
            return "Data Engineer"
        elif y <= 10:
            return "Senior Data Engineer"
        else:
            return "Lead"
    except:
        return "Unknown"

# Phone cleaning logic
def clean_phone(phone):
    try:
        if 'x' in str(phone):
            return "Invalid Number"
        return int(phone)
    except:
        return "Invalid Number"

# Hire date formatting
def format_date(date_str):
    try:
        return pd.to_datetime(date_str).strftime('%Y-%m-%d')
    except:
        return None

# Main function to fetch and normalize data
def normalize_employee_data(data):
    df = pd.DataFrame(data)

    for col in ["first_name", "last_name", "phone", "email", "gender", "age", "job_title",
                "years_of_experience", "salary", "department", "hire_date"]:
        if col not in df.columns:
            df[col] = None

    df["Full Name"] = df["first_name"].fillna('') + " " + df["last_name"].fillna('')
    
    def get_designation(years):
        try:
            y = int(years)
            if y < 3:
                return "System Engineer"
            elif y <= 5:
                return "Data Engineer"
            elif y <= 10:
                return "Senior Data Engineer"
            else:
                return "Lead"
        except:
            return "Unknown"

    df["designation"] = df["years_of_experience"].apply(get_designation)

    def clean_phone(phone):
        try:
            if 'x' in str(phone):
                return "Invalid Number"
            return int(phone)
        except:
            return "Invalid Number"

    df["phone"] = df["phone"].apply(clean_phone)

    def format_date(date_str):
        try:
            return pd.to_datetime(date_str).strftime('%Y-%m-%d')
        except:
            return None

    df["hire_date"] = df["hire_date"].apply(format_date)

    df = df.astype({
        "Full Name": "string",
        "email": "string",
        "gender": "string",
        "age": "Int64",
        "job_title": "string",
        "years_of_experience": "Int64",
        "salary": "Int64",
        "department": "string",
    })

    return df

def scrape_employee_data():
    response = requests.get(API_URL)
    if response.status_code != 200:
        print("Failed to fetch employee data.")
        return pd.DataFrame()

    json_data = response.json()
    if isinstance(json_data, dict) and "data" in json_data:
        data = json_data["data"]
    elif isinstance(json_data, list):
        data = json_data
    else:
        print("Unexpected JSON format.")
        return pd.DataFrame()

    return normalize_employee_data(data)


# Run scraper and save to CSV
if __name__ == "__main__":
    df = scrape_employee_data()
    if not df.empty:
        df.to_csv("employee_data.csv", index=False)
        print(f"Saved {len(df)} employee records to employee_data.csv")
    else:
        print("No data saved.")
