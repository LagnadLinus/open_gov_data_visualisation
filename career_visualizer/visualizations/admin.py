from django.contrib import admin
from .models import EducationData, MentalHealthData, CrimeData, IncomeData


# Register your models here.

@admin.register(EducationData)
class EducationDataAdmin(admin.ModelAdmin):
    list_display = ('education_level', 'family_income', 'year')

@admin.register(MentalHealthData)
class MentalHealthDataAdmin(admin.ModelAdmin):
    list_display = ('mental_health_issues', 'support_needed', 'year')

@admin.register(CrimeData)
class CrimeDataAdmin(admin.ModelAdmin):
    list_display = ('crime_rate', 'year')

@admin.register(IncomeData)
class IncomeDataAdmin(admin.ModelAdmin):
    list_display = ('family_income', 'year')
