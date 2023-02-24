from django import forms
from .models import MealPlan, MiscItem
from recipes.models import Recipe

class RecipeFormMixin:
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['recipes'].queryset = Recipe.objects.filter(owner=user)

class MealPlanForm(RecipeFormMixin, forms.ModelForm):
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
