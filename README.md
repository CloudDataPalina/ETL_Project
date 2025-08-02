# 🚗 Car Price ETL Project

📄 [View full ETL pipeline in Jupyter Notebook](https://github.com/CloudDataPalina/ETL_Project/blob/main/ETL_project.ipynb)


A mini-project demonstrating a complete ETL (Extract–Transform–Load) pipeline using Python. The project loads used car data from multiple file formats (CSV, JSON, XML), performs basic transformations, and saves a cleaned dataset ready for further analysis or integration.

---

## 📁 Project Structure

```
Car-Price-ETL-Project/
├── datasource/                      ← Folder with input CSV, JSON, XML files
│   ├── used_car_prices1.csv
│   ├── used_car_prices1.json
│   ├── used_car_prices1.xml
│   ├── used_car_prices2.csv
│   ├── used_car_prices2.json
│   ├── used_car_prices2.xml
│   ├── used_car_prices3.csv
│   ├── used_car_prices3.json
│   └── used_car_prices3.xml
├── transformed_data.csv            ← Final cleaned dataset
├── log_file.txt                    ← Log of ETL job execution
├── ETL_project.ipynb               ← Full ETL pipeline notebook
└── README.md                       ← Project documentation (this file)

```

## ⚙️ Tools & Technologies

- Python  
- pandas  
- csv  
- json  
- xml.etree.ElementTree  
- glob  
- datetime  
- Jupyter Notebook  

---

## 🔄 ETL Process Overview

### 1️⃣ Extract
- Loads files from the current working directory  
- Handles `.csv`, `.json`, and `.xml` formats  
- Skips the output target file to avoid re-processing already transformed data

### 2️⃣ Transform
- Standardizes column structure
- Rounds `price` column to two decimal places

### 3️⃣ Load
- Exports the final DataFrame to a CSV file → [`transformed_data.xls`](./transformed_data.xls)
- Adds timestamped logs to → [`log_file.txt`](./log_file.txt)
- Source files are located in → [`/datasource`](./datasource/)

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
