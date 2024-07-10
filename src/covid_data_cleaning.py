import os
import pandas as pd
from datetime import datetime


# Reading the file

current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir,'..', 'data')
csv_path = os.path.join(data_path, 'raw', 'WHO-COVID-19-global-data.csv')
world_data_output_path = os.path.join(data_path,'processed', 'covid_19_world')
EURO_data_output_path = os.path.join(data_path,'processed', 'covid_19_EU')

print(f'output directories:\n {world_data_output_path}')

data = pd.read_csv(csv_path)
input_data = data.copy()

print(input_data.info()) # checks the data types

# Cleaning the data (standardizing the format, removing rows with missing values)

input_data["Date_reported"] = pd.to_datetime(input_data["Date_reported"])


# (data.info()) Optional - checks the data types after the format change

# Removing null values (NaN values)
input_data = input_data.dropna(subset=['New_cases', 'Cumulative_cases', 'New_deaths', 
'Cumulative_deaths'])

# Creating separate DataFrames for each year for World data

currentdate = datetime.today().strftime('%Y-%m-%d')
data_2020 = input_data[input_data["Date_reported"].between("2020-01-01", "2020-12-31")]
data_2021 = input_data[input_data["Date_reported"].between("2021-01-01", "2021-12-31")]
data_2022 = input_data[input_data["Date_reported"].between("2022-01-01", "2022-12-31")]
data_2023 = input_data[input_data["Date_reported"].between("2023-01-01", "2023-12-31")]
data_2024 = input_data[input_data["Date_reported"].between("2024-01-01", currentdate)]


# Dictionary with years and data
data_dict = {'2020': data_2020,'2021': data_2021, '2022': data_2022, '2023': data_2023, '2024': data_2024}

timestamp = int(datetime.now().timestamp())

# Create output directories for World data:
output_run_path = os.path.join(world_data_output_path, str(timestamp))
os.makedirs(output_run_path, exist_ok=True)

for year, data in data_dict.items():
    output_file_path = os.path.join(output_run_path, f'data_{year}_{timestamp}.csv')
    data.to_csv(output_file_path, index=False)
    print(f"Saved data for year {year} to {output_run_path}")

### Extracting European Union data from World data into separate files:

eu_countries = [
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", 
    "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", 
    "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", 
    "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"
]

# Creating separate DataFrames for each year for World data

data_EURO = input_data[input_data["WHO_region"]=="EURO"]
data_EU = data_EURO[data_EURO["Country"].isin(eu_countries)]

currentdate = datetime.today().strftime('%Y-%m-%d')
EU_data_2020 = data_EU[data_EU["Date_reported"].between("2020-01-01", "2020-12-31")]
EU_data_2021 = data_EU[data_EU["Date_reported"].between("2021-01-01", "2021-12-31")]
EU_data_2022 = data_EU[data_EU["Date_reported"].between("2022-01-01", "2022-12-31")]
EU_data_2023 = data_EU[data_EU["Date_reported"].between("2023-01-01", "2023-12-31")]
EU_data_2024 = data_EU[data_EU["Date_reported"].between("2024-01-01", currentdate)]


# EU dictionary with years and data:
EU_data_dict = {'2020': EU_data_2020,'2021': EU_data_2021, '2022': EU_data_2022, '2023': EU_data_2023, '2024': EU_data_2024}

# Create output directories and save European Union data:

output_EURO_run_path = os.path.join(EURO_data_output_path, str(timestamp))
os.makedirs(output_EURO_run_path, exist_ok=True)

for year, data in EU_data_dict.items():
    output_EURO_file_path = os.path.join(output_EURO_run_path, f'data_{year}_{timestamp}.csv')
    data.to_csv(output_EURO_file_path, index=False)
    print(f"Saved data for year {year} to {output_run_path}")




