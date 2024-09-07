

import pandas as pd

def load_data():
    education_data = pd.read_csv('visualizations/data/education_data.csv')
    mental_health_data = pd.read_csv('visualizations/data/mental_health_data.csv')
    crime_data = pd.read_csv('visualizations/data/crime_data.csv')
    income_data = pd.read_csv('visualizations/data/income_data.csv')
    return education_data, mental_health_data, crime_data, income_data


def filter_data(year_range, education_level, mental_health_support, crime_rate, income_range):
    # Example of filtering data (adjust as per your data structure)
    # Filter based on year range
    filtered_data = data[(data['year'] >= year_range[0]) & (data['year'] <= year_range[1])]
    
    # Add more filters based on user input
    if education_level:
        filtered_data = filtered_data[filtered_data['education_level'].isin(education_level)]
    if mental_health_support:
        filtered_data = filtered_data[filtered_data['mental_health_support'] == mental_health_support]
    if crime_rate:
        filtered_data = filtered_data[filtered_data['crime_rate'] == crime_rate]
    if income_range:
        filtered_data = filtered_data[(filtered_data['income'] >= income_range[0]) & (filtered_data['income'] <= income_range[1])]
    
    return filtered_data
