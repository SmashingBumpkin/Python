from django import forms
from .models import Recipe

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    img = forms.ImageField()

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','serves', 'description', 'book',
                 'page', 'ingredients_string', 'method']