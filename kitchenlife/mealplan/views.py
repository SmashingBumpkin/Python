from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import MealPlan
from .forms import MealPlanForm, AddItemForm
from recipes.forms import SearchForm

@login_required
def meal_plan_index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            filtered_meal_plan = form.cleaned_data['search_term']
            meal_plan_list = MealPlan.objects.filter(name__contains=filtered_meal_plan, owner=request.user).order_by("name")
    else:
        form = SearchForm()
        meal_plan_list = MealPlan.objects.filter(owner=request.user).order_by("name")
    context = {'meal_plan_list': meal_plan_list, 'form': form}
    return render(request, 'mealplan/meal_plan_index.html', context)

@login_required
def meal_plan_detail(request, meal_plan_id):
    #TODO: Delete mealplan option
    meal_plan = get_object_or_404(MealPlan, id=meal_plan_id, owner=request.user)
    recipe_list = list(meal_plan.recipes.all())
    ingredient_list = list(meal_plan.ingredients.all())
    context = {'meal_plan': meal_plan, 'recipe_list':recipe_list, 'ingredient_list': ingredient_list}
    return render(request, 'mealplan/meal_plan_detail.html', context)

@login_required
def add_meal_plan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            mealplan = form.save(commit=False)
            mealplan.owner = request.user
            mealplan.save()
            form.save_m2m()
            return redirect('mealplan:meal_plan_detail', meal_plan_id=mealplan.id)
    else:
        form = MealPlanForm()
    mealplans = MealPlan.objects.filter(owner=request.user)
    return render(request, 'mealplan/add_meal_plan.html', {'mealplans': mealplans, 'form': form})

@login_required
def edit_meal_plan(request, id):
    #TODO: Break up the ingredients lists by the recipe they go in
    meal_plan = get_object_or_404(MealPlan, id=id, owner=request.user)

    if request.method == 'POST':
        selected_ingredients = request.POST.getlist('ingredients')
        meal_plan.ingredients.set(selected_ingredients)
        meal_plan.save()
        #TODO: add item to meal_plan 
        # added_item_form = AddItemForm(request.POST)
        # if added_item_form.name:
            
        #     pass
        ingredients_owned = set(ingredient for recipe in meal_plan.recipes.all() for ingredient in recipe.uses_ingredient.exclude(id__in=meal_plan.ingredients.all()) )
        profile = request.user.profile
        profile.ingredients_owned.add(*ingredients_owned)
        profile.save()
        return redirect('mealplan:meal_plan_detail', meal_plan_id=id)
    
    selected_ingredients = set(meal_plan.ingredients.all())
    combined_ingredients = []
    for recipe in meal_plan.recipes.all():
        dumb_ingredients = recipe.ingredients_string.split('\n')
        ingredients = list(recipe.uses_ingredient.all())
        for dumb_ingredient in dumb_ingredients:
            for ingredient in ingredients:
                if ingredient.name.lower() in dumb_ingredient.lower():
                    combined_ingredients.append((dumb_ingredient, ingredient, recipe))

    context = {
        'meal_plan': meal_plan,
        'ingredients': combined_ingredients,
        'selected_ingredients': selected_ingredients,
    }
    return render(request, 'mealplan/edit_meal_plan.html', context)