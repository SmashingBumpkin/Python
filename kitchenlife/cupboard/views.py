from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from cupboard.forms import EmptyForm
from kitchenlife.openai_link import sendPrompt
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
    profile = request.user.profile
    owned_by_user = profile.ingredients_owned.filter(id=ingredient.id)
    if request.method == 'POST':
        if not owned_by_user:
            profile.ingredients_owned.add(ingredient)
        else:
            profile.ingredients_owned.remove(ingredient)
        profile.save()
        owned_by_user = profile.ingredients_owned.filter(id=ingredient.id)
    response = sendPrompt("Answer yes or no. Is "+ ingredient.name + " a fruit, a vegetable or a meat?", request.user.profile)
    print(response)
    recipes = ingredient.ingredient_uses.filter(owner = request.user)
    context = {'ingredient': ingredient, 'recipes': recipes, 'owned_by_user': owned_by_user, 'form': EmptyForm}
    return render(request, 'cupboard/ingredient_detail.html', context)

@login_required
def edit_cupboard(request):
    profile = request.user.profile
    if request.method == 'POST':
        ingredients = request.POST.getlist('ingredients')
        profile.ingredients_owned.string_to_ingredients(ingredients)
        profile.save()
        return redirect('cupboard:cupboard_index')
    else:
        ingredients = profile.ingredients_owned.all().order_by("name")
    context = {'ingredients': ingredients}
    return render(request, 'cupboard/edit_cupboard.html', context)