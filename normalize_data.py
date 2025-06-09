import pandas as pd
import json

#load raw data from JSON file
with open("employees.json", "r") as f:
    data = json.load(f)

#to convert JSON data to DataFrame
df = pd.DataFrame(data)

### --- Data Normalization --- ###
#create "Full Name" by combining first & last names
if "first_name" in df.columns and "last_name" in df.columns:
    df["Full Name"] = df["first_name"].str.title() + " " + df["last_name"].str.title()

#now we have to assign Designation Based on Experience
if "years_of_experience" in df.columns:
    df["Designation"] = df["years_of_experience"].apply(lambda x:
        "System Engineer" if x < 3 else
        "Data Engineer" if 3 <= x <= 5 else
        "Senior Data Engineer" if 5 < x <= 10 else
        "Lead"
    )

#validate Phone Numbers
if "phone" in df.columns:
    df["Phone"] = df["phone"].apply(lambda x: "Invalid Number" if "x" in str(x) else x)

#next we convert Data Types
df = df.astype({
    "Full Name": "string",
    "email": "string",
    "Phone": "string",  #handling invalid numbers as strings
    "gender": "string",
    "age": "int",
    "job_title": "string",
    "years_of_experience": "int",
    "salary": "int",
    "department": "string"
}, errors="ignore")

#format "Hire Date" to YYYY-MM-DD
if "Hire Date" in df.columns:
    df["Hire Date"] = pd.to_datetime(df["Hire Date"], errors="coerce").dt.strftime("%Y-%m-%d")

#now save normalized data to CSV
df.to_csv("normalized_employees.csv", index=False)
print("Data normalization completed, File saved as 'normalized_employees.csv'.")