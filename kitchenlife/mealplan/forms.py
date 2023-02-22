from django import forms
from .models import MealPlan

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['name', 'recipes']
        widgets = {
            'recipes': forms.CheckboxSelectMultiple
        }