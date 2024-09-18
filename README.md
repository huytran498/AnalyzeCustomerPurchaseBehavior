# Customer Purchasing Behavior Analysis

This project analyzes customer purchasing behavior data using Python. It performs data cleaning, exploratory data analysis, and generates visualizations to gain insights into customer patterns.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Description](#file-description)
- [Visualizations](#visualizations)

## Installation

To run this project, you need Python 3.6+ and the following libraries:

## Usage

1. Clone this repository:

- git clone https://github.com/yourusername/customer-purchasing-behavior.git

2. Navigate to the project directory:

- cd customer-purchasing-behavior

3. Ensure your data file `Customer Purchasing Behaviors.csv` is in the same directory.

4. Run the script:

5. Check the console output for insights and the generated PNG files for visualizations.

## Features

- Data cleaning (removing duplicates and outliers)
- Basic statistical analysis
- Correlation analysis
- Distribution visualization of numeric variables
- Purchase amount analysis by region and age group
- Top 10 customers by purchase amount

## File Description

- `analysis_script.py`: Main Python script for data analysis
- `CustomerPurchasingBehaviors.csv`: Input data file (not included in repository)
- `README.md`: This file, containing project information

## Visualizations

The script generates the following visualizations:

1. `correlation_matrix.png`: Heatmap of correlations between variables
2. `numeric_distributions.png`: Histograms of all numeric variables
3. `purchase_amount_by_region.png`: Boxplot of purchase amounts across regions
4. `avg_purchase_by_age.png`: Bar plot of average purchase amounts by age group

Check these PNG files after running the script to visualize the results.