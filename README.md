# Employee Scraper Project  

## Overview  
This project scrapes employee details from a public API at  
[https://api.slingacademy.com/v1/sample-data/files/employees.json](https://api.slingacademy.com/v1/sample-data/files/employees.json)  
The scraped data is normalized, validated, and stored in a clean CSV format for analysis.

## Objective  
- Extract fields like **ID, Name, Email, Phone, Designation, Hire Date, and Experience**  
- Normalize data by formatting, merging, and converting fields  
- Store results in a structured file: `normalized_employees.csv`  
- Implement validation and testing using Python’s `unittest` framework  
- Handle invalid phone numbers, format dates, and classify designations  
---
## Technologies Used  
- **Language**: Python  
- **Libraries**: `requests`, `json`, `pandas`, `unittest`, `os`  
- **Storage**: CSV  
- **Tools**: VS Code, GitHub  
---

## Business Flow  
1️. **API Call** – Fetch JSON data from the endpoint  
2️. **Parse & Convert** – Transform JSON into a Pandas DataFrame  
3️. **Data Normalization** –  
   - Merge names into "Full Name"  
   - Classify Designation based on Experience  
   - Replace invalid phone numbers  
   - Format `Hire Date` to `YYYY-MM-DD`  
4️.**Type Conversion** – Match schema with appropriate data types  
5️. **Output** – Save normalized data into `normalized_employees.csv`  
6️. **Testing** – Run unit tests to validate extraction, structure, and quality  
---

## Implementation and Code Structure  

### Key Scripts  
- `main.py`  
  - Central controller script to run the scraper, normalization, and test scripts  
- `normalize_data.py`  
  - Cleans, restructures, and transforms raw employee data  
- `test_scraper.py`  
  - Validates scraping, structure, and quality using Python’s `unittest`
---

## Error Handling  
- **HTTP Failures** – Logged and handled with retry logic (if implemented)  
- **Invalid Phone Numbers** – Any phone containing `'x'` is marked as `"Invalid Number"`  
- **Invalid Dates** – Coerced into standard `YYYY-MM-DD` format or set as `NaT`  
- **Non-200 API Response** – Logged and skipped gracefully  
- **Missing Columns** – Optional fields are handled using safe lookups  
---

## Data Storage (`normalized_employees.csv`)  

| Full Name      | Email                           | Phone            | Gender | Age | Job Title               | Designation      | Experience | Salary | Department | Hire Date  |
|----------------|----------------------------------|------------------|--------|-----|--------------------------|-------------------|------------|--------|------------|------------|
| Jose Lopez     | joselopez0944@slingacademy.com   | Invalid Number   | Male   | 25  | Project Manager          | System Engineer   | 1          | 8500   | Product    | 2018-05-10 |
| Diane Carter   | dianecarter1228@slingacademy.com | 881.633.0107     | Female | 26  | Machine Learning Engineer| System Engineer   | 2          | 7000   | Product    | 2022-04-30 |
| Shawn Foster   | shawnfoster2695@slingacademy.com | Invalid Number   | Male   | 37  | Project Manager          | Lead              | 14         | 17000  | Product    | 2019-09-15 |
---

## Data Normalization Rules

1. **Full Name** = `first_name` + `last_name`  
2. **Designation**:
   - `< 3 yrs` → System Engineer  
   - `3–5 yrs` → Data Engineer  
   - `6–10 yrs` → Senior Data Engineer  
   - `> 10 yrs` → Lead  
3. **Invalid Phone**: If phone contains `'x'`, set as `"Invalid Number"`  
4. **Data Types**:
   - Full Name → `string`  
   - Email → `string`  
   - Phone → `string`  
   - Age, Salary, Experience → `int`  
   - Hire Date → `YYYY-MM-DD`
---

## Testing and Validation  

### Test Cases Covered  
1. **Verify JSON File Exists**  
2. **Validate Data Extraction to DataFrame**  
3. **Check File Format and Field Types**  
4. **Validate Data Structure (Column Headers)**  
5. **Ensure No Missing or Null Data**
---

## Conclusion
This project demonstrates the complete pipeline for scraping, cleaning, and validating employee data from a public API. By applying structured data transformation and implementing logic-based normalization rules, the output is ready for use in real-world analytics and dashboards.

The project also includes built-in testing to ensure data quality and consistency — making it reliable, scalable, and production-ready. This solution can easily be adapted for other datasets with similar JSON structures.
