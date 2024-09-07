


from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64



# Example data loader function
def load_data():
    # Replace with actual data loading logic
    data = pd.DataFrame({
        'education_level': ['None', 'TAFE', 'Masters', 'PhD'],
        'family_income': [40000, 80000, 200000, 250000],
        'crime_rate': ['High', 'Medium', 'Low', 'Very Low'],
        'mental_health_issues': [True, False, True, False]
    })
    return data

def index(request):
    # Example user input
    year_range = (1960, 2023)
    education_level = request.GET.getlist('education')
    mental_health_support = request.GET.get('mentalHealth')
    crime_rate = request.GET.get('crimeRate')
    income_range = (7000, 50000)

    # Filter data based on user input
    filtered_data = filter_data(year_range, education_level, mental_health_support, crime_rate, income_range)

    # Generate the visualization
    img_base64 = generate_visualization(filtered_data)

    # Render the template with the image
    return render(request, 'visualizations/index.html', {'img_base64': img_base64})


def filter_data(year_range, education_level, mental_health_support, crime_rate, income_range):
    data = load_data()
    
    # Apply filters based on the parameters passed
    # Filter by education level
    if education_level:
        data = data[data['education_level'].isin(education_level)]

    # Filter by mental health support
    if mental_health_support == 'true':  # Checkbox sends 'true' as string
        data = data[data['mental_health_issues'] == True]
    elif mental_health_support == 'false':
        data = data[data['mental_health_issues'] == False]

    # Filter by crime rate
    if crime_rate:
        data = data[data['crime_rate'] == crime_rate]

    # Filter by income range
    data = data[(data['family_income'] >= income_range[0]) & (data['family_income'] <= income_range[1])]

    return data


def generate_visualization(filtered_data):
    # Create a simple bar chart for the example (replace with your actual visualization logic)
    plt.figure(figsize=(10, 6))
    
    # Example plot: Visualizing family income
    plt.bar(filtered_data['education_level'], filtered_data['family_income'], color=['red', 'orange', 'green', 'blue'])
    plt.xlabel('Education Level')
    plt.ylabel('Family Income')
    plt.title('Family Income by Education Level')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the image to base64 so it can be embedded in HTML
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    
    return img_base64

