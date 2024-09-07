

from django.db import models


# Create your models here.

class EducationData(models.Model):
    """Model to store education-related data."""
    education_level = models.CharField(max_length=255)  # e.g., 'None', 'TAFE', 'Masters', 'PhD'
    family_income = models.FloatField()  # Family income
    year = models.PositiveIntegerField()  # Year of data

    def __str__(self):
        return f"{self.education_level} - {self.family_income} - {self.year}"

class MentalHealthData(models.Model):
    """Model to store mental health-related data."""
    mental_health_issues = models.BooleanField()  # True if issues present
    support_needed = models.BooleanField()  # True if support needed
    year = models.PositiveIntegerField()  # Year of data

    def __str__(self):
        return f"Mental Health Issues: {self.mental_health_issues}, Support Needed: {self.support_needed}, Year: {self.year}"

class CrimeData(models.Model):
    """Model to store crime rate data."""
    crime_rate = models.CharField(max_length=50)  # e.g., 'High', 'Medium', 'Low', 'Very Low'
    year = models.PositiveIntegerField()  # Year of data

    def __str__(self):
        return f"Crime Rate: {self.crime_rate}, Year: {self.year}"

class IncomeData(models.Model):
    """Model to store family income data."""
    family_income = models.FloatField()  # Family income
    year = models.PositiveIntegerField()  # Year of data

    def __str__(self):
        return f"Income: {self.family_income}, Year: {self.year}"
