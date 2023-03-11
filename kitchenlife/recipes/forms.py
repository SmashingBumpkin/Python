from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe

class UploadFileForm(forms.Form):
    img = forms.ImageField()

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=50)

class QuantityForm(forms.Form):
    quantity = forms.IntegerField()

class EditIngredientsForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['simplified_ingredients']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 30, 'cols': 40}),
        }
        labels = {
            'simplified_ingredients': 'Simplified ingredients'
        }

class UploadURLForm(forms.Form):
    uploadedurl = forms.URLField(label = "Enter recipe URL")

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','serves', 'description', 'book',
                 'page', 'ingredients_string', 'method', 'url']
        
        widgets = {
            'name': forms.TextInput(attrs={"class": "input",}),
            'serves': forms.TextInput(attrs={"class": "input",}),
            'description': forms.Textarea(attrs={"class": "textarea", "rows": 5}),
            'book': forms.TextInput(attrs={"class": "input",}),
            'page': forms.TextInput(attrs={"class": "input",}),
            'ingredients_string': forms.Textarea(attrs={"class": "textarea"}),
            'method': forms.Textarea(attrs={"class": "textarea",}),
            'url': forms.TextInput(attrs={"class": "input",}),
        }
        
        labels = {
            'ingredients_string': "Ingredients"
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
