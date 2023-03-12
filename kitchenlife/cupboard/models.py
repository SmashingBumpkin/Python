from django.db import models
from re import split as resplit

from kitchenlife.unit_and_number_handling import convert_to_grams

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    long_life = models.BooleanField(null= True, blank=True)
    shelf_life = models.IntegerField(null= True, blank=True)
    substitutes = models.CharField(max_length = 200, null = True, blank= True)
    category = models.CharField(max_length=60, null= True, blank=True)
    calories = models.IntegerField(default = 0)
    carbohydrates = models.FloatField(default = 0)
    sugar = models.FloatField(default = 0)
    fat = models.FloatField(default = 0)
    protein = models.FloatField(default = 0)
    fibre = models.FloatField(default = 0)
    typical_weight = models.IntegerField(null= True, blank=True)

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
                    print("number extracter returns: "+result)
                    break
            if result:
                print(result)
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
                elif "substitutes" in detail_lower:
                    self.substitutes = detail.split(":")[1].strip()
                elif "long life" in detail_lower:
                    detail_lower = detail_lower.split(":")[1].strip()
                    if "yes" in detail_lower:
                        self.long_life = True
                    elif "no" in detail_lower:
                        self.long_life = False
                elif "shelf life" in detail_lower:
                    detail_lower = detail_lower.split(":")[1].strip()
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
                    self.category = detail.split(":")[1].strip()
                elif "typical weight" in detail_lower:
                    detail_lower= detail_lower.split(":")[1].strip()
                    number = extract_number(detail_lower)
                    self.typical_weight = int(number)
                elif "calories" in detail_lower:
                    detail_lower= detail_lower.split(":")[1].strip()
                    number = extract_number(detail_lower)
                    self.calories = int(number)
                elif "carbohydrates" in detail_lower:
                    detail_lower= detail_lower.split(":")[1].strip()
                    number = extract_number(detail_lower)
                    self.carbohydrates = number
                elif "sugar" in detail_lower:
                    detail_lower= detail_lower.split(":")[1].strip()
                    number = extract_number(detail_lower)
                    self.sugar = number
                elif "fat" in detail_lower:
                    detail_lower= detail_lower.split(":")[1].strip()
                    number = extract_number(detail_lower)
                    self.fat = number
                elif "protein" in detail_lower:
                    detail_lower= detail_lower.split(":")[1].strip()
                    number = extract_number(detail_lower)
                    self.protein = number
                elif "fibre" in detail_lower:
                    detail_lower= detail_lower.split(":")[1].strip()
                    number = extract_number(detail_lower)
                    self.fibre = number
            except:
                pass
        self.save()
    
    def return_nutrition(self, quantity, unit):
        quantity = convert_to_grams(quantity, unit) # returns 
        scale = quantity/100
        jeff = [self.calories,self.carbohydrates,self.sugar,self.fat,self.protein, self.fibre]
        for jef in jeff:
            if jef == None:
                jef = 0
        output = {"calories": scale*jeff[0],
                  "carbohydrates": scale*jeff[1],
                  "sugar": scale*jeff[2],
                  "fat": scale*jeff[3],
                  "protein": scale*jeff[4],
                  "fibre": scale*jeff[5],}
        return output