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
    book = models.CharField(max_length=200, null = True, blank = True)
    page = models.CharField(max_length=5, null = True, blank = True)
    serves = models.CharField(max_length=5, null = True, blank = True)
    serves_int = models.IntegerField(null = True, blank = True)
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
        print("UPDATING INGREDIENTS LINK")
        #Function that generates a the RecipeIngredients that link this recipe to the ingredients
        self.recipe_ingredient.all().delete()
        ingredients_list = list(resplit("\n|,", self.simplified_ingredients))
        #print(ingredients_list)
        dumb_ingredients_list = self.ingredients_string.lower().split('\n')
        #TODO:
        #If the number of dumb ingredient lines matches the number of simplified ingredients:
        #   Simple algo to match each ingredient up, then assign quantity and units and everything to the subingredient class
        #If there are more simplified ingredients than dumb ingredients
        #   Find the shared lines and parse somehow
        #Order ingredients so they can be returned correctly
        #Find a pairing for each ingredient to each dumb ingredient
        #Save the info of quantity, unit and details to a local instance of the Ingredient variable
        for i in range(len(ingredients_list)):
            ingredients_list[i] = ingredients_list[i].strip().lower()
            if ingredients_list[i] == "":
                continue
            try:
                ingredient = Ingredient.objects.get(name=ingredients_list[i].capitalize())
            except:
                ingredient = Ingredient(name = ingredients_list[i].capitalize())
                ingredient.save()
                response = openai_link.sendPromptIngredientDetails(ingredient.name, active_user)
                ingredient.ai_response_parser(response)
        
        #ingredients_list = set(ingredients_list)
        line_number = 10 # line number 
        for dumb_line in dumb_ingredients_list:
            for ingredient_name in ingredients_list:
                if ingredient_name in dumb_line:
                    alternative = False #Used for when an alternative ingredient is suggested
                    ingredients_list.remove(ingredient_name)
                    ingredients_list.append(ingredient_name)
                    if " and " in dumb_line:
                        #Special handling to check for 2 (or more??) ingredients in a line
                        for ingredient_name_2 in ingredients_list: # searches for the second ingredient in the line
                            if ingredient_name_2 == ingredient_name:
                                continue
                            if ingredient_name_2 in dumb_line:
                                #ingredients_list.remove(ingredient_name_2)
                                dumb_line_2 = dumb_line.split(" and ")
                                line_number -= 3
                                for line in dumb_line_2: #Figures out which line is which
                                    if ingredient_name_2 in line:
                                        ingredient=Ingredient.objects.get(name=ingredient_name_2.strip().capitalize())
                                        recipe_ingredient = RecipeIngredient.parse_dumb_ingredient(recipe=self, ingredient=ingredient,ingredient_dumb=line)
                                        recipe_ingredient.position_in_list = line_number
                                        recipe_ingredient.save()
                                    else:
                                        dumb_line = line
                                    line_number += 6
                                line_number -= 9
                                break #END SPECIAL "AND" HANDLING

                    elif " or " in dumb_line:
                        #Special handling to check for 2 ingredients in a line
                        for ingredient_name_2 in ingredients_list:
                            if ingredient_name_2 == ingredient_name:
                                continue
                            if ingredient_name_2 in dumb_line:
                                line_number -= 3
                                dumb_line_2 = dumb_line.split(" or ")
                                alt_ingred = dumb_line
                                first_loop = True
                                for line in dumb_line_2:
                                    if ingredient_name_2 in line:
                                        #print("OR " + line)
                                        alt_ingred = alt_ingred.replace(" or ", " ")
                                        alt_ingred = alt_ingred.replace(ingredient_name + " ", "")
                                        alt_ingred = alt_ingred.replace(" " + ingredient_name, "")
                                        ingredient=Ingredient.objects.get(name=ingredient_name_2.strip().capitalize())
                                        recipe_ingredient = RecipeIngredient.parse_dumb_ingredient(recipe=self, ingredient=ingredient,ingredient_dumb=alt_ingred)
                                        recipe_ingredient.alternative = not first_loop
                                        recipe_ingredient.position_in_list = line_number
                                        recipe_ingredient.save()
                                        alternative = first_loop
                                    else:
                                        dumb_line = dumb_line.replace(" or ", " ")
                                        dumb_line = dumb_line.replace(ingredient_name_2 + " ", "")
                                        dumb_line = dumb_line.replace(" " + ingredient_name_2, "")
                                    first_loop = False
                                    line_number += 6
                                line_number -= 9
                                break 
                        #END SPECIAL "OR" HANDLING

                    #Parse recipe ingredient from line
                    ingredient=Ingredient.objects.get(name=ingredient_name.strip().capitalize())
                    recipe_ingredient = RecipeIngredient.parse_dumb_ingredient(recipe=self, ingredient=ingredient,ingredient_dumb=dumb_line)
                    recipe_ingredient.alternative = alternative
                    recipe_ingredient.position_in_list = line_number
                    recipe_ingredient.save()
                    line_number += 10
                    break
            
            #ingredient.referenced_by_profile.add(active_user.profile)
            #ingredient.save()
    
    def serves_to_int(self):
        """
        This function takes a string as input and returns a number contained within the string, if it exists.
        The number can be an integer or a float.
        """
        result = ''
        for char in self.serves:
            if char.isdigit():
                result += char
            elif result != '':
                break
        if result:
            self.serves_int = int(result)

    def method_as_list(self):
        try:
            method_as_list = self.method.split('\n')
            if method_as_list[0][0] != "1":
                method_as_list = [str(i+1) + ". " + step for i, step in enumerate(method_as_list)]
        except:
            method_as_list = []
        return method_as_list
    
    
    #TODO: Implement a function to rate recipes

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredient")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe_ingredient")
    quantity = models.FloatField(null=True, blank=True)
    measurement_unit = models.CharField(max_length=50, null=True, blank=True)
    local_name = models.CharField(max_length=100)
    position_in_list = models.IntegerField(null=True, blank=True)
    optional = models.BooleanField(default = False)
    alternative = models.BooleanField(default = False)
    
    def __str__(self):
        output = ""
        if self.optional:
            output = "(Optional) "
        if self.alternative:
            output = "(Alternative) "
        if self.quantity: #removes unnecessary decimals from float
            qty = str(self.quantity)
            qty =qty.rstrip('0').rstrip('.') if '.' in qty else qty
            output += qty + " "
        if self.measurement_unit:
            output = output[:-1]
            output += self.measurement_unit + " "
        output += self.local_name
        return output.capitalize()
    
    def scaled_string(self, scale):
        output = ""
        if self.optional:
            output = "(Optional) "
        if self.alternative:
            output = "(Alternative) "
        if self.quantity: #removes unnecessary decimals from float
            scaled_qty = str(round(self.quantity*scale, 2))
            qty = scaled_qty.rstrip('0').rstrip('.') if '.' in scaled_qty else scaled_qty
            output += qty + " "
        if self.measurement_unit:
            output = output[:-1]
            output += self.measurement_unit + " "
        output += self.local_name
        return output.capitalize()


    def parse_dumb_ingredient(recipe, ingredient, ingredient_dumb,):
        #TODO Check for import errors, eg Y = 1/, % = 1/2 or 1/3
        L = refindall(r'\d+|\D+',  ingredient_dumb) #Splits string into list of ints+strings
        if len(L) == 1:
            return RecipeIngredient(recipe=recipe,ingredient=ingredient,local_name=ingredient_dumb)
        
        #gets posn of first int
        posn = next((i for i, x in enumerate(L) if x.isdigit()), None)
        #tries to parse quantity
        if posn+2 < len(L) and (L[posn+1] in {".",","}):
            quantity = float("".join(L[posn:posn+3]))
            posn += 2
        elif L[posn+1] == "/":
            quantity = float(Fraction("".join(L[posn:posn+3])))
            posn += 2
        elif L[posn+1] == " " and L[posn+3] == "/":
            #TODO: Improve resiliance
            quantity = float(int(L[posn])+Fraction("".join(L[posn+2:posn+5])))
            posn += 4
        else:
            quantity = float(L[posn])
        
        posn += 1
        #Checks for import error on quantity (99.9% chance this is import error)
        if recipe.from_photo:
            if quantity > 100 and quantity % 10 == 9:
                quantity = (quantity - 9)/10
                L[posn] = "g" + L[posn]
            elif quantity > 100 and quantity %100 == 2:
                quantity = (quantity - 2)/100
                L[posn] = "oz" + L[posn]
            elif quantity > 10 and L[posn][0] == "z":
                #TODO: This import error handling is not very resilient
                quantity = quantity/10
                L[posn] = "o" + L[posn]
        
        units = {"grams","g","tbsp","tablespoon","tsp","teaspoon","kg","l","ml","liters","milliliters","oz", 
                 "ounce","ounces","lb","pound","pounds","cup","cups","pint","quart","floz"}
        #gets what's left of string after quantity removed
        remaining_string = "".join(L[posn:]).lower().strip()

        #Finds units if they are present
        L[posn] = L[posn].lower()
        try:
            first_word = refindall(r'\w+', L[posn])[0]
        except:
            first_word = None
        if first_word in units:
            unit = first_word.strip()
            remaining_string = remaining_string[remaining_string.index(unit) + len(unit):].strip().capitalize()
            return RecipeIngredient(recipe=recipe,ingredient=ingredient,local_name=remaining_string,
                                    quantity=quantity,measurement_unit=unit)
        else:
            unit = ""
            return RecipeIngredient(recipe=recipe,ingredient=ingredient,local_name=remaining_string,
                                    quantity=quantity)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name="profile")
    ingredients_referenced = models.ManyToManyField(Ingredient, related_name="referenced_by_profile", blank=True) # every ingredient ever used by this user
    ingredients_owned = models.ManyToManyField(Ingredient,related_name="owned_by_profile", blank=True) # ingredients currently available to this user
    ai_credits_used = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    def ingredients_owned_list(self):
        return [ingredient.name for ingredient in self.ingredients_owned.all()]