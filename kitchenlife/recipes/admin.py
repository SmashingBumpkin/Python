from django.contrib import admin

from .models import Recipe, Ingredient, Profile, MealPlan

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Profile)
admin.site.register(MealPlan)