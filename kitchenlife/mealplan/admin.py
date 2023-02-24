from django.contrib import admin
from .models import MealPlan, MiscItem

# Register your models here.
admin.site.register(MealPlan)
admin.site.register(MiscItem)