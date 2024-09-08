

import pandas as pd

def load_data():
    # Load your datasets
    education_data = pd.read_csv('visualizations/data/education_data.csv')
    mental_health_data = pd.read_csv('visualizations/data/mental_health_data.csv')
    crime_data = pd.read_csv('visualizations/data/crime_data.csv')
    income_data = pd.read_csv('visualizations/data/income_data.csv')

    # Merge the datasets if necessary (assuming all datasets have a 'year' column)
    merged_data = education_data.merge(mental_health_data, on='year')
    merged_data = merged_data.merge(crime_data, on='year')
    merged_data = merged_data.merge(income_data, on='year')

    return merged_data

def filter_data(year_range, education_levels, crime_rate, income_range, mental_health):
    data = load_data()

    # Filter by year range
    data = data[(data['year'] >= year_range[0]) & (data['year'] <= year_range[1])]

    # Filter by education level
    if education_levels:
        data = data[data['parents_education'].isin(education_levels)]

    # Filter by mental health issues
    if mental_health:
        data = data[data['mental_health_support'] == True]

    # Filter by crime rate
    if crime_rate:
        data = data[data['crime_rate'].isin(crime_rate)]

    # Filter by income range
    data = data[(data['family_income'] >= income_range[0]) & (data['family_income'] <= income_range[1])]

    return data
