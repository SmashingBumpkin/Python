from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Recipe

def index(request):
    recipe_list = Recipe.objects.all()
    template = loader.get_template('recipes/index.html')
    context = {'recipe_list': recipe_list}
    return render(request, 'recipes/index.html', context)


def detail(request, recipe_id):
    return HttpResponse("You're looking at recipe %s." % recipe_id)

def add_recipe(request):
    return HttpResponse("Hello, world. You're at the add recipe page.")
