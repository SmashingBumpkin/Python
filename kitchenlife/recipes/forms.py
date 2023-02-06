from django import forms
from .models import Recipe

class UploadFileForm(forms.Form):
    img = forms.ImageField()

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','serves', 'description', 'book',
                 'page', 'ingredients_string', 'method']