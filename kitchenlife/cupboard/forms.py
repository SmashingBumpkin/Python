from django import forms

from recipes.models import ProfileIngredient

class EmptyForm(forms.Form):
    pass


class EditProfileIngredientForm(forms.ModelForm):
    class Meta:
        model = ProfileIngredient
        fields = ['long_life_override','shelf_life_override', 'substitutes_override', 'category_override',
                 'calories_override', 'carbohydrates_override', 'sugar_override', 'fat_override', 'protein_override',
                 'fibre_override', 'typical_weight_override']
        
        widgets = {
            'long_life_override': forms.CheckboxInput(attrs={"class": "checkbox"}),
            'shelf_life_override': forms.NumberInput(attrs={"class": "input","placeholder":"Shelf life"}),
            'substitutes_override': forms.TextInput(attrs={"class": "input","placeholder":"Substitutes"}),
            'category_override': forms.TextInput(attrs={"class": "input","placeholder":"Category"}),
            'calories_override': forms.NumberInput(attrs={"class": "input","placeholder":"Calories"}), 
            'carbohydrates_override': forms.NumberInput(attrs={"class": "input","placeholder":"Carbohydrates"}), 
            'sugar_override': forms.NumberInput(attrs={"class": "input","placeholder":"Sugar"}), 
            'fat_override': forms.NumberInput(attrs={"class": "input","placeholder":"Fat"}), 
            'protein_override': forms.NumberInput(attrs={"class": "input","placeholder":"Protein"}),
            'fibre_override': forms.NumberInput(attrs={"class": "input","placeholder":"Fibre"}),
            'typical_weight_override': forms.NumberInput(attrs={"class": "input","placeholder":"Typical weight"}),
        }
        
        labels = {
            'long_life_override': 'Long life:',
            'shelf_life_override': 'Shelf life:',
            'substitutes_override': 'Substitutes:',
            'category_override': 'Category:',
            'calories_override': 'Calories per 100g:', 
            'carbohydrates_override': 'Carbohydrates per 100g:', 
            'sugar_override': 'Sugar override per 100g:',
            'fat_override': 'Fat per 100g:', 
            'protein_override': 'Protein per 100g:',
            'fibre_override': 'Fibre per 100g:',
            'typical_weight_override': 'Typical weight:'
        }