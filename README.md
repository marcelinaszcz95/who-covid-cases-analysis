# WHO Covid-10 cases analysis with Python
WHO Covid-19 cases analysis with Python and Tableu

## Overview

This repository contains a script for data analysis using Python. The script is designed to process and analyze data, with examples focused on COVID-19 case data from WHO.

## Features

 - Data extraction
 - Data cleaning
 - Summary output files generation

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries:
  - pandas
  - os
  - datetime

You can install the required libraries using:

pip install 

## Installation

    - Clone the repository:

git clone https://github.com/marcelinaszcz95/who-covid-cases-analysis.git

    - Navigate to the project directory:

cd who-covid-cases-analysis

## Data Source

This project uses data provided by the World Health Organization (WHO). The data is freely available and can be accessed [here](https://data.who.int/dashboards/covid19/data).

**Attribution:** World Health Organization. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Usage
    - Ensure the data file is located in the data/raw directory.
    - Run the analysis script: python src/covid_data_cleaning.py

This will process the raw data, perform the analysis, and generate the output csv files with clean, sorted data for further visualizations with Tableau. The script generates World data, and also EU data. To generate only World data you can comment out the rest of the code.

## Output
Cleaned data files in data/processed

