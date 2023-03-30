from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from cupboard.forms import EditProfileIngredientForm, EmptyForm
from kitchenlife.openai_link import sendPromptForgottenDetails, sendPromptIngredientDetails
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
    profile = request.user.profile
    profile_ingredient = profile.profile_ingredient.get(ingredient = ingredient)
    profile_ingredient.check_and_remove_expired()
    nutrients = profile_ingredient.get_nutrition(100, "g")
    if request.method == 'POST':
        profile_ingredient.in_stock = not profile_ingredient.in_stock
        profile_ingredient.save()
    
    try:
        days_until_expiry = (profile_ingredient.expiry_date - date.today()).days
    except:
        days_until_expiry = 0
    recipes = Recipe.objects.filter(recipe_ingredient__profile_ingredient=profile_ingredient)
    context = {'ingredient': ingredient,
               'profile_ingredient': profile_ingredient,
               'recipes': recipes, 
               'owned_by_user': profile_ingredient.in_stock, 
               'form': EmptyForm,
               'time_to_expiry': days_until_expiry,
               'nutrients': nutrients,}
    return render(request, 'cupboard/ingredient_detail.html', context)

@login_required
def edit_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    profile = request.user.profile
    profile_ingredient = profile.profile_ingredient.get(ingredient = ingredient)
    initial_ingredient = profile_ingredient.get_ingredient_info_as_profileingredient()
    if request.method == 'POST':
        modifications_have_been_made = False
        if "save_ingredient_updates" in request.POST:
            form = EditProfileIngredientForm(request.POST)
            if form.is_valid():
                for override_key in initial_ingredient.keys():
                    form_value = form.cleaned_data[override_key]
                    initial_value = initial_ingredient[override_key]
                    if form_value != initial_value:
                        setattr(profile_ingredient, override_key, form_value)
                        modifications_have_been_made = True
            if modifications_have_been_made:
                profile_ingredient.save()
        elif "reset_to_defaults" in request.POST:
            profile_ingredient.reset_overrides()
            modifications_have_been_made = True
        if modifications_have_been_made:
            initial_ingredient = profile_ingredient.get_ingredient_info_as_profileingredient()
        return redirect('cupboard:ingredient_detail', ingredient_id=ingredient_id)
        
    form = EditProfileIngredientForm(initial = initial_ingredient)
    return render(request, 'cupboard/edit_ingredient.html', {'form':form})

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