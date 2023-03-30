from django.db import models
from re import split as resplit
from kitchenlife.openai_link import sendPromptIngredientDetails

from kitchenlife.unit_and_number_handling import convert_to_grams

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    long_life = models.BooleanField(default= True) #overwritable
    shelf_life = models.IntegerField(default = 14) #overwritable
    substitutes = models.CharField(max_length = 200, blank= True) #overwritable
    category = models.CharField(max_length=60, blank=True) #overwritable
    calories = models.IntegerField(default = 0) #overwritable
    carbohydrates = models.FloatField(default = 0) #overwritable
    sugar = models.FloatField(default = 0) #overwritable
    fat = models.FloatField(default = 0)#overwritable
    protein = models.FloatField(default = 0)#overwritable
    fibre = models.FloatField(default = 0)#overwritable
    typical_weight = models.IntegerField(default = 0)#overwritable

    def __str__(self):
        return self.name
    
    def print_variables(self):
        print(f"Name: {self.name}")
        print(f"Substitutes: {self.substitutes}")
        print(f"Long Life: {self.long_life}")
        print(f"Shelf Life: {self.shelf_life}")
        print(f"Category: {self.category}")
        print(f"Typical weight: {self.typical_weight}")
        print("Nutritional information per 100g/ml:")
        print(f"Calories: {self.calories}")
        print(f"Carbohydrates: {self.carbohydrates}")
        print(f"Sugar: {self.sugar}")
        print(f"Fat: {self.fat}")
        print(f"Protein: {self.protein}")
        print(f"Fibre: {self.fibre}")

    def reimport_data(self, profile):
        sendPromptIngredientDetails(self.name, profile)
    
    def ai_response_parser(self, response):
        def extract_number(string):
            """
            This function takes a string as input and returns a number contained within the string, if it exists.
            The number can be an integer or a float.
            """
            result = ''
            decimal_point_count = 0
            for char in string:
                if char.isdigit() or char == '.':
                    if char == '.':
                        decimal_point_count += 1
                    if decimal_point_count > 1:
                        return None
                    result += char
                elif result != '':
                    # print("number extracter returns: "+result)
                    break
            if result:
                # print(result)
                return float(result)
            else:
                return 0

        details_list = list(resplit("\n", response))
        for detail in details_list:
            detail = detail.strip()
            detail_lower = detail.lower()
            try:
                if detail == "":
                    continue
                else:
                    detail_value = detail.split(":")[1].strip()
                    detail_lower_value = detail_lower.split(":")[1].strip()
                    if "substitutes" in detail_lower:
                        self.substitutes = detail_value
                    elif "long life" in detail_lower:
                        detail_lower = detail_lower_value
                        if "yes" in detail_lower:
                            self.long_life = True
                        elif "no" in detail_lower:
                            self.long_life = False
                    elif "shelf life" in detail_lower:
                        detail_lower = detail_lower_value
                        number = extract_number(detail_lower)
                        if "year" in detail_lower:
                            self.shelf_life = int(number*365)
                        elif "month" in detail_lower:
                            self.shelf_life = int(number*30)
                        elif "week" in detail_lower:
                            self.shelf_life = int(number*7)
                        elif number:
                            self.shelf_life = int(number)
                    elif "category" in detail_lower:
                        self.category = detail_value
                    elif "typical weight" in detail_lower:
                        detail_lower= detail_lower_value
                        number = extract_number(detail_lower)
                        self.typical_weight = int(number)
                    elif "calories" in detail_lower:
                        detail_lower= detail_lower_value
                        number = extract_number(detail_lower)
                        self.calories = int(number)
                    elif "carbohydrates" in detail_lower:
                        detail_lower= detail_lower_value
                        number = extract_number(detail_lower)
                        self.carbohydrates = number
                    elif "sugar" in detail_lower:
                        detail_lower= detail_lower_value
                        number = extract_number(detail_lower)
                        self.sugar = number
                    elif "fat" in detail_lower:
                        detail_lower= detail_lower_value
                        number = extract_number(detail_lower)
                        self.fat = number
                    elif "protein" in detail_lower:
                        detail_lower= detail_lower_value
                        number = extract_number(detail_lower)
                        self.protein = number
                    elif "fibre" in detail_lower:
                        detail_lower= detail_lower_value
                        number = extract_number(detail_lower)
                        self.fibre = number
            except:
                pass
        self.save()