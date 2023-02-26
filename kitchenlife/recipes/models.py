from django.db import models
from django.contrib.auth.models import User
from kitchenlife import openai_link
from cupboard.models import Ingredient
from re import split as resplit
from sys import exit as sysexit


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    method = models.TextField(max_length=5000, null = True, blank = True)
    ingredients_string = models.TextField(max_length=1000, null = True, blank = True)#Plain text of ingredients
    book = models.CharField(max_length=200, null = True, blank = True)
    page = models.CharField(max_length=5, null = True, blank = True)
    serves = models.CharField(max_length=5, null = True, blank = True)
    description = models.TextField(max_length=500, null = True, blank = True)
    url = models.URLField(null = True, blank = True)
    jumbled_input = models.TextField(max_length=8000, null = True, blank = True)
    simplified_ingredients = models.TextField(max_length=1000, null = True, blank = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    uses_ingredient = models.ManyToManyField(Ingredient, related_name="ingredient_uses")

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
    
    def string_to_ingredients(self, active_user):
        myprompt = ("Take this list of ingredients, and return a simple list containing only "
                + "raw ingredients seperated by ',': \n\n"
                + self.ingredients_string)
        text = openai_link.sendPrompt(myprompt, model = "text-curie-001", temperature=0.7)
        print("\n____\n" + text)
        cont = input("\n____\n\nIf text is correct press 1 to continue ")
        if cont != "1":
            text = input("Write corrected list below, seperating ingredients by ',': \n")
        self.simplified_ingredients = text
        ingredientsList = resplit("\n| or |,| and ", text)
        for ingredientName in ingredientsList:
            ingredientName = ingredientName.strip().capitalize()
            if ingredientName != "":
                try:
                    ingredient = Ingredient.objects.get(name=ingredientName)
                except:
                    ingredient = Ingredient(name = ingredientName)
                    ingredient.save()
                ingredient.ingredient_uses.add(self)
                ingredient.referenced_by_profile.add(active_user.profile)
                #active_user.ingredients_referenced.add(ingredient)
                ingredient.save()
    
    def simplify_ingredients(self):
        myprompt = ("Take this list of ingredients for a recipe, and simplify it by returning a " +
                "list containing only the raw ingredients seperated by '\\n': \n\n"
                + self.ingredients_string)
        self.simplified_ingredients = openai_link.sendPrompt(myprompt, model = "text-curie-001", temperature=0.7)

    def simplified_to_ingredients(self, active_user):
        ingredientsList = resplit("\n| or |,| and ", self.simplified_ingredients)
        for ingredientName in ingredientsList:
            ingredientName = ingredientName.strip().capitalize()
            if ingredientName != "":
                try:
                    ingredient = Ingredient.objects.get(name=ingredientName)
                except:
                    ingredient = Ingredient(name = ingredientName)
                    ingredient.save()
                ingredient.ingredient_uses.add(self)
                ingredient.referenced_by_profile.add(active_user.profile)
                #active_user.ingredients_referenced.add(ingredient)
                ingredient.save()

    def method_as_list(self):
        try:
            method_as_list = self.method.split('\n')
            method_as_list = [str(i+1) + ". " + step for i, step in enumerate(method_as_list)]
        except:
            method_as_list = []
        return method_as_list
    
    def caps_remover(self):
        #TODO: makea function to reformat stuff to not be all caps
        pass
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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name="profile")
    ingredients_referenced = models.ManyToManyField(Ingredient, related_name="referenced_by_profile", blank=True) # every ingredient ever used by this user
    ingredients_owned = models.ManyToManyField(Ingredient,related_name="owned_by_profile", blank=True) # ingredients currently available to this user

    def __str__(self):
        return self.user.username