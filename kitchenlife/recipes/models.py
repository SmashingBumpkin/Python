from django.db import models
from django.contrib.auth.models import User
from kitchenlife import openai_link
from cupboard.models import Ingredient
from re import split as resplit, findall as refindall, sub as resub
from sys import exit as sysexit
from fractions import Fraction


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    method = models.TextField(max_length=5000, null = True, blank = True)
    ingredients_string = models.TextField(max_length=1000, null = True, blank = True)#Plain text of ingredients
    simplified_ingredients = models.TextField(max_length=1000, null = True, blank = True)#Ingredients data
    uses_ingredient = models.ManyToManyField(Ingredient, related_name="ingredient_uses")
    book = models.CharField(max_length=200, null = True, blank = True)
    page = models.CharField(max_length=5, null = True, blank = True)
    serves = models.CharField(max_length=5, null = True, blank = True)
    description = models.TextField(max_length=500, null = True, blank = True)
    url = models.URLField(null = True, blank = True)
    jumbled_input = models.TextField(max_length=8000, null = True, blank = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    from_photo = models.BooleanField(default=False)

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
    
    def simplify_ingredients(self, active_user):
        self.simplified_ingredients = openai_link.sendPromptIngredients(self.ingredients_string, active_user = active_user.profile)

    def simplified_to_ingredients(self, active_user):
        ingredientsList = resplit("\n| or |,| and ", self.simplified_ingredients)
        #TODO:
        #If the number of dumb ingredient lines matches the number of simplified ingredients:
        #   Simple algo to match each ingredient up, then assign quantity and units and everything to the subingredient class
        #If there are more simplified ingredients than dumb ingredients
        #   Find the shared lines and parse somehow
        #Order ingredients so they can be returned correctly
        #Find a pairing for each ingredient to each dumb ingredient
        #Save the info of quantity, unit and details to a local instance of the Ingredient variable
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

# class RecipeIngredient(models.Model):
#     recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name="recipe_ingredient")
#     ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, related_name="recipe_ingredient")
#     quantity = models.FloatField(null=True, blank=True)
#     measurement_unit = models.CharField(max_length=50, null=True, blank=True)
#     string = models.CharField(max_length=100,null=True, blank=True)
#     position_in_list = models.IntegerField(null=True, blank=True)
    
#     class Meta:
#         unique_together = ('recipe', 'ingredient',)


#     def parse_dumb_ingredient(ingredient_dumb):
#         #TODO Check for import errors, eg Y = 1/, % = 1/2 or 1/3
#         L = refindall(r'\d+|\D+',  ingredient_dumb) #Splits string into list of ints+strings
#         if len(L) == 1: #If length is 1, there is nothing to parse
#             ingredient_dumb = resub(r'^\W+', '', ingredient_dumb)
#             print("1 " + ingredient_dumb)
#             return None
        
#         if not any(c.isalnum() for c in L[0]):#Removes start of string if it's eg " -  "
#             L = L[1:]
        
#         #gets posn of first int
#         posn = next((i for i, x in enumerate(L) if x.isdigit()), None)
#         #tried to parse quantity
#         if posn+2 < len(L) and (L[posn+1] in {".",","}):
#             quantity = float("".join(L[posn:posn+3]))
#             posn += 2
#         elif L[posn+1] == "/":
#             quantity = float(Fraction("".join(L[posn:posn+3])))
#             posn += 2
#         elif L[posn+1] == " " and L[posn+3] == "/":
#             #TODO: Improve resiliance
#             quantity = float(int(L[posn])+Fraction("".join(L[posn+2:posn+5])))
#             posn += 4
#         else:
#             quantity = float(L[posn])
        
#         #Checks for import error on quantity (99.9% chance this is import error)
#         if quantity > 100 and quantity % 10 == 9:
#             quantity = (quantity - 9)/10
#             L[posn+1] = "g" + L[posn+1]
        
#         posn += 1
#         units = {"grams","g","tbsp","tsp", "kg", "l", "ml", "liters","milliliters"}
#         #gets what's left of string after quantity removed
#         remaining_string = "".join(L[posn:]).lower().strip()

#         #Finds units if they are present
#         L[posn] = L[posn].lower()
#         try:
#             first_word = refindall(r'\w+', L[posn])[0]
#         except:
#             first_word = None
#         if first_word in units:
#             unit = first_word
#             remaining_string = remaining_string[remaining_string.index(unit) + len(unit):].strip()
#             print(quantity,unit, remaining_string)
#         else:
#             unit = ""
#             print(quantity,remaining_string)
#         return quantity, unit    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name="profile")
    ingredients_referenced = models.ManyToManyField(Ingredient, related_name="referenced_by_profile", blank=True) # every ingredient ever used by this user
    ingredients_owned = models.ManyToManyField(Ingredient,related_name="owned_by_profile", blank=True) # ingredients currently available to this user
    ai_credits_used = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    def ingredients_owned_list(self):
        return [ingredient.name for ingredient in self.ingredients_owned.all()]