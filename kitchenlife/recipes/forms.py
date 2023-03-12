from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe

class PlaintextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'cols': 80, 
                                                        "placeholder":"Paste in an unformatted recipe, we'll handle the rest"}),
                                                        label="")
    
class UploadFileForm(forms.Form):
    img = forms.ImageField()

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=50)

class QuantityForm(forms.Form):
    serving = forms.IntegerField()

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
            'name': forms.TextInput(attrs={"class": "input","placeholder":"Enter recipe name here"}),
            'serves': forms.TextInput(attrs={"class": "input","placeholder":"How many servings does this make?"}),
            'description': forms.Textarea(attrs={"class": "textarea", "rows": 5, "placeholder":"A short description of the recipe"}),
            'book': forms.TextInput(attrs={"class": "input","placeholder":"What book is this recipe from?"}),
            'page': forms.TextInput(attrs={"class": "input","placeholder":"What page of the book?"}),
            'ingredients_string': forms.Textarea(attrs={"class": "textarea","placeholder":"This should be the ingredients as it appears in the recipe"}),
            'method': forms.Textarea(attrs={"class": "textarea","placeholder":"This should be the method for the recipe"}),
            'url': forms.TextInput(attrs={"class": "input","placeholder":"The website URL goes here"}),
        }
        
        labels = {
            'ingredients_string': "Ingredients"
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
