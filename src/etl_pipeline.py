#pip install pandas 

import pandas as pd                   # Working with tabular data (DataFrame)
import glob                           # Finding all files matching a pattern (*.csv, *.json, *.xml)
import xml.etree.ElementTree as ET    # Parsing and working with XML structure

from datetime import datetime         # Adding timestamps to the log
import matplotlib.pyplot as plt       # For data visualization

# === VARIABLES ===
log_file = "output/log_file.txt"             # File to log the progress of the ETL process
target_file = "output/transformed_data.csv"  # Final CSV file with the transformed data


def log_progress(message):
    timestamp_format = '%Y-%b-%d-%H:%M:%S'      # Timestamp format, e.g. 2025-Jul-26-19:45:04
    now = datetime.now()                        # Get the current time
    timestamp = now.strftime(timestamp_format)  # Format the time as a string
    with open(log_file, "a") as f:              # Open the log file in append mode
        f.write(f"{timestamp},{message}\n")     # Write the timestamp and message to the file


def extract_from_csv(file_to_process):
    return pd.read_csv(file_to_process)  # Reading a CSV file into a DataFrame using pandas


def extract_from_json(file_to_process):
    # Reads a JSON file line by line in JSON Lines format (each line is a separate JSON object)
    return pd.read_json(file_to_process, lines=True)


def extract_from_xml(file_to_process):
    # Create an empty DataFrame with predefined columns and data types
    # Using pd.Series(dtype=...) to explicitly define the structure
    dataframe = pd.DataFrame({
        "car_model": pd.Series(dtype="str"),            # string
        "year_of_manufacture": pd.Series(dtype="int"),  # integer
        "price": pd.Series(dtype="float"),              # float
        "fuel": pd.Series(dtype="str")                  # string
    })

    # Load and parse the XML file
    tree = ET.parse(file_to_process)    # create XML tree object
    root = tree.getroot()               # get root element of the XML structure

    # Iterate over each item (e.g., <car>) within the root
    for i in root:
        # Extract values from sub-elements of the current element
        car_model = i.find("car_model").text
        year_of_manufacture = int(i.find("year_of_manufacture").text)
        price = float(i.find("price").text)
        fuel = i.find("fuel").text

        # Build a dictionary from the extracted values
        row = {
            "car_model": car_model,
            "year_of_manufacture": year_of_manufacture,
            "price": price,
            "fuel": fuel
        }

        # Append the new row to the DataFrame
        dataframe.loc[len(dataframe)] = row

    # Return the final DataFrame with data extracted from XML
    return dataframe


def extract():
    # Create an empty DataFrame with predefined columns and data types
    extracted_data = pd.DataFrame({
        "car_model": pd.Series(dtype="str"),               # Car brand/model
        "year_of_manufacture": pd.Series(dtype="int"),     # Year of manufacture
        "price": pd.Series(dtype="float"),                 # Price
        "fuel": pd.Series(dtype="str")                     # Fuel type
    })

    # === Extract data from CSV files ===
    for csvfile in glob.glob("data/*.csv"):                     # Loop through all .csv files in the current directory
        if csvfile != target_file:                         # Skip the final output file to avoid recursive processing
            new_data = extract_from_csv(csvfile)           # Extract data using extract_from_csv()
            if not new_data.empty:                         # Only process if the result is not empty
                # Append to the main DataFrame
                # ignore_index=True resets row indices (0 to N-1) after concatenation
                extracted_data = pd.concat([extracted_data, new_data], ignore_index=True)

    # === Extract data from JSON files ===
    for jsonfile in glob.glob("data/*.json"):                   # Loop through all .json files
        new_data = extract_from_json(jsonfile)             # Extract data from file
        if not new_data.empty:                           # Skip empty results
            extracted_data = pd.concat([extracted_data, new_data], ignore_index=True)

    # === Extract data from XML files ===
    for xmlfile in glob.glob("data/*.xml"):                     # Loop through all .xml files
        new_data = extract_from_xml(xmlfile)               # Extract data from file
        if not new_data.empty:                           # Skip empty results
            extracted_data = pd.concat([extracted_data, new_data], ignore_index=True)

    return extracted_data                                   # Return the merged DataFrame


def transform(data):
    # Transform the 'price' column by rounding values to two decimal places
    data['price'] = round(data['price'], 2)
    return data  # Return the transformed DataFrame

def load_data(target_file, transformed_data):
    # Save the transformed data to a CSV file without including the index
    transformed_data.to_csv(target_file, index=False)

# === RUNNING THE ETL PIPELINE ===
log_progress("ETL Job Started")

# Extract phase
log_progress("Extract phase Started")
extracted_data = extract()
log_progress("Extract phase Ended")

# Transform phase
log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data:")
print(transformed_data)
log_progress("Transform phase Ended")

# Load phase
log_progress("Load phase Started")
load_data(target_file, transformed_data)
log_progress("Load phase Ended")

# Completion
log_progress("ETL Job Ended")


# === 1. Average Price by Brand ===

# Extract the car brand from the 'car_model' column:
# take the first word (usually the brand) and convert it to lowercase
transformed_data["brand"] = transformed_data["car_model"].str.split().str[0].str.lower()

# Group by brand and calculate the average price for each
avg_price_by_brand = transformed_data.groupby("brand")["price"].mean()

# Select the top 10 brands with the highest average prices
top_brands = avg_price_by_brand.sort_values(ascending=False).head(10)

# Print the table with prices rounded to 2 decimal places
print("Top 10 car brands by average price:")
print(top_brands.round(2))

# Build a horizontal bar chart
plt.figure(figsize=(9, 4.5))                                                       # set figure size
plt.barh(top_brands.index.str.title(), top_brands.values, color="mediumseagreen")  # plot bars
plt.xlabel("Average Price (USD)")                                                  # X-axis label
plt.title("Top 10 Most Expensive Used Car Brands")                                 # chart title
plt.gca().invert_yaxis()                                                           # invert Y-axis to show most expensive on top
plt.tight_layout()                                                                 # optimize spacing
plt.savefig("images/top_brands_avg_price.png")                                     # save the chart to file
plt.show()                                                                         # display the chart



# === 2. Average Price by Year of Manufacture ===

# Group the data by year of manufacture and calculate the average price for each year
avg_price_by_year = transformed_data.groupby("year_of_manufacture")["price"].mean()

# Print the table with average prices by year, rounded to 2 decimal places
print("Average price by year of manufacture:")
print(avg_price_by_year.round(2))

# Create a line chart:
plt.figure(figsize=(9, 4.5))  # set the figure size

# Plot the line: X-axis = year of manufacture, Y-axis = average price
plt.plot(avg_price_by_year.index, avg_price_by_year.values,
         marker="o", linestyle='-', color='steelblue')

# Add title and axis labels
plt.title("Average Car Price by Year of Manufacture")
plt.xlabel("Year of Manufacture")
plt.ylabel("Average Price (USD)")

# Add grid lines for better readability
plt.grid(True)

# Adjust layout to prevent clipping
plt.tight_layout()

# Save the chart to the output folder
plt.savefig("images/avg_price_by_year.png")

# Display the chart
plt.show()

