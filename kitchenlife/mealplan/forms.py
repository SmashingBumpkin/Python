from django import forms
from .models import MealPlan, MiscItem

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['name', 'recipes']
        widgets = {
            'recipes': forms.CheckboxSelectMultiple
        }

class AddItemForm(forms.ModelForm):
    class Meta:
        model = MiscItem
        fields = ['name', 'quantity']
