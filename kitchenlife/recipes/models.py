from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    method = models.TextField(max_length=2000)
    ingredients_string = models.TextField(max_length=500)#Plain text of ingredients
    book = models.CharField(max_length=200, null = True, blank = True)
    page = models.CharField(max_length=5, null = True, blank = True)
    serves = models.CharField(max_length=5, null = True, blank = True)
    description = models.TextField(max_length=200, null = True, blank = True)
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
                    }
    
    #TODO: Implement a method that can extract ingredients from
    #       ingredient string, if necessary create the ingredients, 
    #       and link them to the recipe
    #TODO: Implement a function to rate recipes


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)
    ingredient_uses = models.ManyToManyField(Recipe)
    def __str__(self):
        return self.ingredient_name