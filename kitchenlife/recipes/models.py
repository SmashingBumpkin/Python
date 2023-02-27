from django.db import models
from django.contrib.auth.models import User
from kitchenlife import openai_link
from cupboard.models import Ingredient
from re import split as resplit
from re import findall as refindall
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
    
    class Ingredient(Ingredient):
        recipe_str_a = models.CharField(max_length=200, null=True, blank=True)
        recipe_int_b = models.IntegerField(null=True, blank=True)
        recipe_str_c = models.CharField(max_length=200, null=True, blank=True)
        recipe_int_d = models.IntegerField(null=True, blank=True)
        recipe_str_e = models.CharField(max_length=200, null=True, blank=True)
        recipe_int_f = models.IntegerField(null=True, blank=True)
        recipe_str_g = models.CharField(max_length=200, null=True, blank=True)
        recipe_int_h = models.IntegerField(null=True, blank=True)
        recipe_str_i = models.CharField(max_length=200, null=True, blank=True)
        
        def __str__(self):
            pass

        def string_to_ingredient(self, line):
            parts = refindall(r'\d+|\D+', line)
            combined_list = [int(p) if p.isdigit() else p for p in parts]
            if type(combined_list[0]) == str:
                self.recipe_str_a = combined_list[0]
                combined_list = combined_list[1:]
            else:
                self.recipe_str_a = ""
            
            try:
                self.recipe_int_b = combined_list[0]
                self.recipe_str_c = combined_list[1]
                self.recipe_int_d = combined_list[2]
                self.recipe_str_e = combined_list[3]
                self.recipe_int_f = combined_list[4]
                self.recipe_str_g = combined_list[5]
                self.recipe_int_h = combined_list[6]
                self.recipe_str_i = combined_list[7]
            except:
                pass

        def ingredient_string(self):
            return (self.recipe_int_b + self.recipe_str_c + self.recipe_int_d + self.recipe_str_e 
                    + self.recipe_int_f + self.recipe_str_g + self.recipe_int_h + self.recipe_str_i
                    + self.recipe_int_j)
        
            
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
    
    def simplify_ingredients(self, active_user):
        myprompt = ("Take this list of ingredients for a recipe, and simplify it by returning a " +
                "list containing only the raw ingredients seperated by '\\n': \n\n"
                + self.ingredients_string)
        self.simplified_ingredients = openai_link.sendPrompt(myprompt, active_user = active_user.profile, model = "text-curie-001", temperature=0.7)

    def simplified_to_ingredients(self, active_user):
        ingredientsList = resplit("\n| or |,| and ", self.simplified_ingredients)
        for ingredientName in ingredientsList:
            ingredientName = ingredientName.strip().capitalize()
            if ingredientName == "":
                continue
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
            if method_as_list[0][0] != "1":
                method_as_list = [str(i+1) + ". " + step for i, step in enumerate(method_as_list)]
        except:
            method_as_list = []
        return method_as_list
    
    def caps_remover(self):
        #TODO: makea function to reformat stuff to not be all caps
        pass
    #TODO: Implement a function to rate recipes

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name="profile")
    ingredients_referenced = models.ManyToManyField(Ingredient, related_name="referenced_by_profile", blank=True) # every ingredient ever used by this user
    ingredients_owned = models.ManyToManyField(Ingredient,related_name="owned_by_profile", blank=True) # ingredients currently available to this user
    ai_credits_used = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    def ingredients_owned_list(self):
        return [ingredient.name for ingredient in self.ingredients_owned.all()]