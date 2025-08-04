# 🚗 Car Price ETL Project
![status](https://img.shields.io/badge/status-passed-brightgreen)

### ✅ Project Status
This project is **functionally complete and tested**, but **open for future improvements and enhancements**.

📄 [View full ETL pipeline in Jupyter Notebook](https://github.com/CloudDataPalina/ETL_Project/blob/main/ETL_project.ipynb)


A mini-project demonstrating a complete ETL (Extract–Transform–Load) pipeline using Python. The project loads used car data from multiple file formats (CSV, JSON, XML), performs basic transformations, and saves a cleaned dataset ready for further analysis or integration.

---

## 📁 Project Structure

```
Car-Price-ETL-Project/
├── data/                                   ← Folder with input CSV, JSON, XML files
│ ├── used_car_prices1.csv
│ ├── used_car_prices1.json
│ ├── used_car_prices1.xml
│ ├── used_car_prices2.csv
│ ├── used_car_prices2.json
│ ├── used_car_prices2.xml
│ ├── used_car_prices3.csv
│ ├── used_car_prices3.json
│ └── used_car_prices3.xml
├── output/
│ ├── transformed_data.csv                  ← Final cleaned dataset
│ └── log_file.txt                          ← Log of ETL job execution
├── src/
│ └── etl_pipeline.py                       ← Python version of ETL logic
├── ETL_project.ipynb                       ← Full ETL pipeline in Jupyter Notebook
├── requirements.txt                        ← Project dependencies
└── README.md                               ← Project documentation (this file)
```


---

## 🛠️ Skills & Tools

- `Python` : core programming language
- `pandas` : data transformation and manipulation
- `csv` : reading and writing tabular data
- `json` : working with JSON-formatted data
- `xml.etree.ElementTree` : XML parsing and extraction
- `glob` : pattern-based file searching
- `datetime` : working with dates and timestamps
- `Jupyter Notebook` : interactive coding and documentation
- `matplotlib` : visual analytics and charts
  
---

## 🔄 ETL Process Overview

### 1️⃣ Extract
- Loads files from the `/datasource` folder  
- Supports `.csv`, `.json`, and `.xml` formats  
- Skips already transformed output file to prevent duplication

### 2️⃣ Transform
- Standardizes the column names
- Cleans data types and rounds prices to 2 decimal places

### 3️⃣ Load
- Saves final data to: [`output/transformed_data.csv`](https://github.com/CloudDataPalina/ETL_Project/blob/main/output/transformed_data.csv)  
- Logs operations in: [`output/log_file.txt`](https://github.com/CloudDataPalina/ETL_Project/blob/main/output/log_file.txt)

---

## 📊 Visual Insights

Using `matplotlib`, the project generates key charts:

- **Top 10 Car Brands by Average Price**  
   [`images/top_brands_avg_price.png`](https://github.com/CloudDataPalina/ETL_Project/blob/main/images/top_brands_avg_price.png)

- **Average Price by Year of Manufacture**  
   [`images/avg_price_by_year.png`](https://github.com/CloudDataPalina/ETL_Project/blob/main/images/avg_price_by_year.png)

### 📌 Key Insights:

- The most expensive brands include **Toyota** and **Suzuki**
- Cars manufactured in **2020 and later** maintain the highest average prices
- There is a clear inverse relationship between vehicle age and price — **the newer the car, the higher its market value**

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/CloudDataPalina/ETL_Project.git
cd ETL_Project
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Python script
```bash
python src/etl_pipeline.py
```
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

- **Extracted** data from `.csv`, `.json`, and `.xml` files  
- **Transformed** prices and standardized the dataset for consistency  
- **Loaded** the result into a clean `.csv` file for further analysis  
- 🧾 All actions were logged for traceability  
- 📊 **Visualized key insights** using matplotlib — including average prices by brand and year

This project demonstrates how a simple yet complete ETL and analytics pipeline can uncover valuable insights from heterogeneous data sources.

---

## 👩‍💻 Author

**Palina Krasiuk**  
Aspiring Cloud Data Engineer | ex-Senior Accountant  
[LinkedIn](https://www.linkedin.com/in/palina-krasiuk-954404372/) • [GitHub Portfolio](https://github.com/CloudDataPalina)
