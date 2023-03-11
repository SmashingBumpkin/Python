from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from cupboard.forms import EmptyForm
from kitchenlife.openai_link import sendPrompt, sendPromptForgottenDetails, sendPromptIngredientDetails, sendPromptTypicalShelfLife, sendPromptTypicalWeight
from recipes.models import Recipe
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

    # ingredients = Ingredient.objects.filter().order_by("name")
    # for ingred in ingredients:
        # if ingred.name[0].lower() == "s": 
        #     if ingred.name[1] > "a": 
                # jeff = sendPromptTypicalShelfLife(ingred.name, request.user)
                # ingred.shelf_life = extract_number(jeff.strip())
                # ingred.save()
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
    # ingredient.print_variables()
    # ingredient.ai_response_parser(sendPromptIngredientDetails(ingredient.name, request.user))
    #ingredient.print_variables()
    profile = request.user.profile
    owned_by_user = profile.ingredients_owned.filter(id=ingredient.id)
    if request.method == 'POST':
        if not owned_by_user:
            profile.ingredients_owned.add(ingredient)
        else:
            profile.ingredients_owned.remove(ingredient)
        profile.save()
        owned_by_user = profile.ingredients_owned.filter(id=ingredient.id)
    recipes = set(Recipe.objects.filter(recipe_ingredient__ingredient__name=ingredient.name, owner = request.user))
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