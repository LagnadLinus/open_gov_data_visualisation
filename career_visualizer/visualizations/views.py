import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
import os
from django.conf import settings

def load_csv_data():
    # Define file paths
    crime_file = os.path.join(settings.BASE_DIR, 'datas', 'crime_data.csv')
    education_file = os.path.join(settings.BASE_DIR, 'datas', 'education_data.csv')
    income_file = os.path.join(settings.BASE_DIR, 'datas', 'income_data.csv')
    mental_health_file = os.path.join(settings.BASE_DIR, 'datas', 'mental_health_data.csv')
    
    # Load CSV files into DataFrames
    crime_data = pd.read_csv(crime_file)
    education_data = pd.read_csv(education_file)
    income_data = pd.read_csv(income_file)
    mental_health_data = pd.read_csv(mental_health_file)

    return crime_data, education_data, income_data, mental_health_data

def index(request):
    return render(request, 'visualizations/index.html')

def get_data(request):
    crime_data, education_data, income_data, mental_health_data = load_csv_data()

    # Convert data to JSON format
    crime_json = crime_data.to_dict(orient='records')
    education_json = education_data.to_dict(orient='records')
    income_json = income_data.to_dict(orient='records')
    mental_health_json = mental_health_data.to_dict(orient='records')

    # Return JSON response
    return JsonResponse({
        'crime': crime_json,
        'education': education_json,
        'income': income_json,
        'mental_health': mental_health_json
    })

def filter_data(request):
    # Define the paths to your CSV files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    crime_data_path = os.path.join(base_dir, 'data', 'crime_data.csv')
    education_data_path = os.path.join(base_dir, 'data', 'education_data.csv')
    income_data_path = os.path.join(base_dir, 'data', 'income_data.csv')
    mental_health_data_path = os.path.join(base_dir, 'data', 'mental_health_data.csv')

    # Read the CSV files into DataFrames
    crime_data = pd.read_csv(crime_data_path)
    education_data = pd.read_csv(education_data_path)
    income_data = pd.read_csv(income_data_path)
    mental_health_data = pd.read_csv(mental_health_data_path)

    # Example: Merging or processing the data as required
    # Here you should filter or process the data based on request parameters

    # Example response
    response_data = {
        "example_field": "example_value",
        # Add more fields based on your data and requirements
    }

    return JsonResponse(response_data)
