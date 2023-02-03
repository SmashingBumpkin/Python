from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_method = models.CharField(max_length=1000)
    #pub_date = models.DateTimeField('date published')
    ingredients_string = models.CharField(max_length=200)#Plain text of ingredients
    def __str__(self):
        return self.recipe_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)
    ingredient_uses = models.ManyToManyField(Recipe)
    def __str__(self):
        return self.ingredient_name