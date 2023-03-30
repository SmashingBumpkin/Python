from django.db import models
from cupboard.models import Ingredient
from recipes.models import Recipe, User

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)
    ingredients = models.ManyToManyField(Ingredient)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
class MiscItem(models.Model):
    name = models.CharField(max_length=50, blank = True)
    quantity = models.IntegerField(null= True, blank = True)
    owner = models.ForeignKey(MealPlan, on_delete=models.CASCADE, blank=True, null=True, related_name = "misc_item")

    def __str__(self):
        return self.name
    