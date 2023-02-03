from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Recipe

def index(request):
    recipe_list = Recipe.objects.all()
    template = loader.get_template('recipes/index.html')
    context = {'recipe_list': recipe_list}
    return render(request, 'recipes/index.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def add_recipe(request):
    recipe_name = "test"
    recipe_method = "try to test"
    ingredients_string = "1 test"
    new_recipe = Recipe.objects.create(recipe_name = recipe_name, 
        recipe_method = recipe_method, ingredients_string = ingredients_string)
    return HttpResponse("Hello, world. You're at the add recipe page.")
