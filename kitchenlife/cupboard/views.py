from datetime import date
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
            profile_ingredient_list = profile.profile_ingredient.filter(ingredient__name__icontains=filtered_ingredient).order_by("ingredient__name")
    else:
        form = SearchForm()
        profile_ingredient_list = profile.profile_ingredient.filter().order_by("ingredient__name")
    # ingredients = Ingredient.objects.filter().order_by("name")
    # for ingred in ingredients:
        # if ingred.name[0].lower() == "s": 
        #     if ingred.name[1] > "a": 
                # jeff = sendPromptTypicalShelfLife(ingred.name, request.user)
                # ingred.shelf_life = extract_number(jeff.strip())
                # ingred.save()
    context = {'profile_ingredient_list': profile_ingredient_list, 'form': form}
    return render(request, 'cupboard/ingredients_index.html', context)

@login_required
def cupboard_index(request):
    profile = request.user.profile
    profile.remove_expired_items()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            filtered_ingredient = form.cleaned_data['search_term']
            profile_ingredient_list = profile.profile_ingredient.filter(in_stock = True, ingredient__name__icontains=filtered_ingredient).order_by("ingredient__name")
    else:
        form = SearchForm()
        profile_ingredient_list = profile.profile_ingredient.filter(in_stock = True).order_by("ingredient__name")
    context = {'profile_ingredient_list': profile_ingredient_list, 'form': form}
    return render(request, 'cupboard/ingredients_index.html', context)

@login_required
def ingredient_detail(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    # ingredient.print_variables()
    # ingredient.ai_response_parser(sendPromptIngredientDetails(ingredient.name, request.user))
    #ingredient.print_variables()
    profile = request.user.profile
    profile_ingredient = profile.profile_ingredient.get(ingredient = ingredient)
    profile_ingredient.check_and_remove_expired()
    if request.method == 'POST':
        profile_ingredient.in_stock = not profile_ingredient.in_stock
        profile_ingredient.save()
    # recipes = set(Recipe.objects.filter(recipe_ingredient__ingredient__profileingredient__profile__user=request.user, recipe_ingredient__ingredient__ingredient__name=ingredient.name))
    

    # Assuming "expiry_date" is a valid date object stored in a variable named "expiry_date"
    try:
        days_until_expiry = (profile_ingredient.expiry_date - date.today()).days
    except:
        days_until_expiry = 0
    recipes = Recipe.objects.filter(recipe_ingredient__profile_ingredient=profile_ingredient)
    context = {'ingredient': ingredient,
               'recipes': recipes, 
               'owned_by_user': profile_ingredient.in_stock, 
               'form': EmptyForm,
               'time_to_expiry': days_until_expiry}
    return render(request, 'cupboard/ingredient_detail.html', context)

@login_required
def edit_cupboard(request):
    profile = request.user.profile
    profile_ingredient_list = profile.profile_ingredient.filter(in_stock=True).order_by("ingredient__name")
    if request.method == 'POST':
        profile_ingredients_to_keep = request.POST.getlist('ingredients')
        # Set all ingredients not in profile_ingredients_to_keep to in_stock=False
        for profile_ingredient in profile_ingredient_list:
            if str(profile_ingredient.ingredient.id) not in profile_ingredients_to_keep:
                profile_ingredient.in_stock = False
                profile_ingredient.save()
        # profile_ingredients_to_keep = request.POST.getlist('ingredients')
        # profile.ingredients_owned.remove(*profile_ingredients_to_keep)
        # profile.save()
        return redirect('cupboard:cupboard_index')
        
    # else:
    #     profile_ingredient_list = profile.profile_ingredient.filter(in_stock = True).order_by("ingredient__name")
    context = {'profile_ingredients': profile_ingredient_list}
    return render(request, 'cupboard/edit_cupboard.html', context)