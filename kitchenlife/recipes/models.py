from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    method = models.CharField(max_length=1000)
    ingredients_string = models.CharField(max_length=200)#Plain text of ingredients
    book = models.CharField(max_length=200, null = True, blank = True)
    page = models.CharField(max_length=5, null = True, blank = True)
    serves = models.CharField(max_length=5, null = True, blank = True)
    description = models.CharField(max_length=200, null = True, blank = True)
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)
    ingredient_uses = models.ManyToManyField(Recipe)
    def __str__(self):
        return self.ingredient_name