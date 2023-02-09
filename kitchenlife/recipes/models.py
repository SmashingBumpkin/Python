from django.db import models
from kitchenlife import openai_link
from re import split as resplit
from sys import exit as sysexit


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    method = models.TextField(max_length=5000)
    ingredients_string = models.TextField(max_length=1000)#Plain text of ingredients
    book = models.CharField(max_length=200, null = True, blank = True)
    page = models.CharField(max_length=5, null = True, blank = True)
    serves = models.CharField(max_length=5, null = True, blank = True)
    description = models.TextField(max_length=500, null = True, blank = True)
    url = models.URLField(null = True, blank = True)
    jumbled_input = models.TextField(max_length=8000, null = True, blank = True)
    simplified_ingredients = models.TextField(max_length=1000, null = True, blank = True)

    def __str__(self):
        return self.name
    
    def return_dict(self):
        return {
                        'name': self.name,
                        'method':self.method,
                        'serves':self.serves,
                        'description':self.description,
                        'book':self.book,
                        'page':self.page,
                        'ingredients_string':self.ingredients_string,
                        'method':self.method,
                        'url': self.url,
                    }
    
    def string_to_ingredients(self):
        myprompt = ("Take this list of ingredients, and return a simple list containing only "
                + "raw ingredients seperated by ',': \n\n"
                + self.ingredients_string)
        text = openai_link.sendPrompt(myprompt, model = "text-curie-001", temperature=0.7)
        print("\n____\n" + text)
        cont = input("\n____\n\nIf text is correct press 1 to continue ")
        if cont != "1":
            text = input("Write corrected list below, seperating ingredients by ',': \n")
        self.simplified_ingredients = text
        ingredientsList = resplit("\n| or |,", text)
        for ingredientName in ingredientsList:
            ingredientName = ingredientName.strip().capitalize()
            if ingredientName != "":
                try:
                    ingredient = Ingredient.objects.get(ingredient_name=ingredientName)
                except:
                    ingredient = Ingredient(ingredient_name = ingredientName)
                    ingredient.save()
                ingredient.ingredient_uses.add(self)
                ingredient.save()
                
    #TODO: Implement a function to rate recipes

def tempingredients():
    return """onion
carrot
celery stick
olive oil
rosemary
'nduja
tomato purée
cherry tomatoes
chicken stock
cannellini beans
ditalini or macaroni
cavolo nero
Parmesan
Salt
black pepper"""


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)
    ingredient_uses = models.ManyToManyField(Recipe)
    #TODO: create way to reference ingredient uses from the recipe
    def __str__(self):
        return self.ingredient_name