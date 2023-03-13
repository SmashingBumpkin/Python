from django.contrib import admin

from .models import ProfileIngredient, Recipe, Profile, RecipeIngredient

admin.site.register(Recipe)
admin.site.register(Profile)
admin.site.register(RecipeIngredient)
admin.site.register(ProfileIngredient)