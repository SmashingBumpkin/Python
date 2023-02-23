from django import forms
from .models import MealPlan

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['name', 'recipes']
        widgets = {
            'recipes': forms.CheckboxSelectMultiple
        }

class AddItemForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    quantity = forms.CharField(max_length=15)
