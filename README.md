# 🚗 Car Price ETL Project

📄 [View full ETL pipeline in Jupyter Notebook](https://github.com/CloudDataPalina/Car-Price-ETL-Project/blob/main/ETL_project.ipynb)

A mini-project demonstrating a complete ETL (Extract–Transform–Load) pipeline using Python. The project loads used car data from multiple file formats (CSV, JSON, XML), performs basic transformations, and saves a cleaned dataset ready for further analysis or integration.

---

## 📁 Project Structure

''' Car-Price-ETL-Project/
├── datasource.zip ← Archive with input CSV, JSON, XML files
├── transformed_data.csv ← Final cleaned dataset
├── log_file.txt ← Log of ETL job execution
├── ETL_project.ipynb ← Full ETL pipeline notebook
└── README.md ← Project documentation (this file) '''


---

## ⚙️ Tools & Technologies

- Python
- pandas
- json
- xml.etree.ElementTree
- zipfile
- Jupyter Notebook

---

## 🔄 ETL Process Overview

### 1️⃣ Extract
- Reads files from a ZIP archive
- Handles `.csv`, `.json`, and `.xml` formats
- Skips the target output file to prevent recursion

### 2️⃣ Transform
- Standardizes column structure
- Rounds `price` column to two decimal places

### 3️⃣ Load
- Exports the final DataFrame to a CSV file (`transformed_data.csv`)
- Adds timestamped logs to `log_file.txt`

---

## 📊 Sample Output (transformed_data.csv)

| car_model   | year_of_manufacture | price    | fuel   |
|-------------|---------------------|----------|--------|
| swift       | 2014                | 6865.67  | Diesel |
| ciaz        | 2015                | 10074.63 | Petrol |
| alto 800    | 2017                | 4253.73  | Petrol |
| ertiga      | 2016                | 11567.16 | Diesel |
| sx4         | 2010                | 3955.22  | Petrol |

---

## ✅ Summary

In this mini-project:

- ✅ **Extracted** data from `.csv`, `.json`, and `.xml` files  
- ✅ **Transformed** prices for consistency  
- ✅ **Loaded** the result into a clean `.csv` file  
- 🧾 All actions are logged for traceability

This project showcases how to build a simple yet complete ETL pipeline for diverse data sources. It serves as a foundation for more advanced data engineering workflows.

---

## 👩‍💻 Author

**Palina Krasiuk**  
Aspiring Cloud Data Engineer | ex-Senior Accountant  
[LinkedIn](https://www.linkedin.com/in/palina-krasiuk-954404372/) • [GitHub Portfolio](https://github.com/CloudDataPalina)
