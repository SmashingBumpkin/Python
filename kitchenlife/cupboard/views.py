from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Ingredient
from recipes.forms import SearchForm

@login_required
def ingredients_index(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            filtered_ingredient = form.cleaned_data['search_term']
            ingredient_list = profile.ingredients_referenced.filter(name__contains=filtered_ingredient).order_by("name")
    else:
        form = SearchForm()
        ingredient_list = profile.ingredients_referenced.filter().order_by("name")
    context = {'ingredient_list': ingredient_list, 'form': form}
    return render(request, 'cupboard/ingredients_index.html', context)

@login_required
def cupboard_index(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            filtered_ingredient = form.cleaned_data['search_term']
            ingredient_list = profile.ingredients_owned.filter(name__contains=filtered_ingredient).order_by("name")
    else:
        form = SearchForm()
        ingredient_list = profile.ingredients_owned.all().order_by("name")
    context = {'ingredient_list': ingredient_list, 'form': form}
    return render(request, 'cupboard/ingredients_index.html', context)

@login_required
def ingredient_detail(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    recipes = ingredient.ingredient_uses.filter(owner = request.user)
    context = {'ingredient': ingredient, 'recipes': recipes}
    return render(request, 'cupboard/ingredient_detail.html', context)