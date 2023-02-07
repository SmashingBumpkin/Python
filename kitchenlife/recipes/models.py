from django.db import models
from kitchenlife import openai_link
from re import split as resplit


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    method = models.TextField(max_length=2000)
    ingredients_string = models.TextField(max_length=500)#Plain text of ingredients
    book = models.CharField(max_length=200, null = True, blank = True)
    page = models.CharField(max_length=5, null = True, blank = True)
    serves = models.CharField(max_length=5, null = True, blank = True)
    description = models.TextField(max_length=200, null = True, blank = True)
    url = models.URLField(null = True, blank = True)
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
        #TODO: FINISH FUNCTION
        myprompt = ("Remove all units of measurement from this list of ingredients, "
                + "seperate the ingredients with '\\n': \n\n"
                + self.ingredients_string)
        #text = openai_link.sendPrompt(myprompt)
        text = tempingredients()
        ingredientsList = resplit("\n|or", text)
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