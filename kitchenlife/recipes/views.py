from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import MealPlan, Recipe, Ingredient
from .forms import MealPlanForm, UploadFileForm, EditRecipeForm, SearchForm, UploadURLForm
from PIL import Image
from . import new_recipe_processing


@login_required
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            filtered_recipe = form.cleaned_data['search_term']
            recipe_list = Recipe.objects.filter(name__contains=filtered_recipe, owner=request.user).order_by("name")
    else:
        form = SearchForm()
        recipe_list = Recipe.objects.filter(owner=request.user).order_by("name")
    context = {'recipe_list': recipe_list, 'form': form}
    return render(request, 'recipes/index.html', context)


@login_required
def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.owner != request.user:
        return redirect('recipes:index')
    method_as_list = recipe.method.split('\n')
    dumb_ingredients = recipe.ingredients_string.split('\n')
    ingredients = list(recipe.uses_ingredient.all())
    combined_ingredients = []
    for dumb_ingredient in dumb_ingredients:
        for ingredient in ingredients:
            if ingredient.name.lower() in dumb_ingredient.lower():
                combined_ingredients.append((dumb_ingredient, ingredient))
                break
                
    context = {'recipe': recipe, 'method_as_list': method_as_list, 'combined_ingredients': combined_ingredients}
    return render(request, 'recipes/detail.html', context)


@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['img'])
            text = new_recipe_processing.image_to_string(img)
            recipe = new_recipe_processing.text_to_recipe(text)
            form = EditRecipeForm(initial = recipe.return_dict())
            return render(request, "recipes/edit_recipe.html", {"form": form})

    elif request.method == 'POST':
        form = EditRecipeForm(request.POST)
        return save_and_redirect_recipe(form, request)
    else:
        form = UploadFileForm()

    return render(request, 'recipes/upload.html', {'form': form})


@login_required
def upload_url(request):
    if request.method == 'POST':
        uploadForm = UploadURLForm(request.POST.copy())
        if uploadForm.is_valid() and uploadForm.cleaned_data['uploadedurl']:
            filtered_url = uploadForm.cleaned_data['uploadedurl']
            recipe = new_recipe_processing.url_to_recipe(filtered_url)
            form = EditRecipeForm(initial = recipe.return_dict())
            return render(request, "recipes/edit_recipe.html", {"form": form})
        else:
            editForm = EditRecipeForm(request.POST)
            if editForm.is_valid():
                return save_and_redirect_recipe(editForm, request)
            else:
                print("ERROR: Submitted form was invalid\n\n\n")
                print(editForm.errors)
                print("\n\n\n")

    form = UploadURLForm()
    return render(request, 'recipes/upload.html', {'form': form})


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.owner != request.user:
        return redirect('recipes:index')

    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance= recipe)
        if form.is_valid():
            #TODO: compare new ingredients to old ingredients
            #       add new ones to db
            #       remove link to removed ingredients
            form.save()
            return redirect('recipes:detail', recipe_id=recipe_id)
    form = EditRecipeForm(initial = recipe.return_dict())
    return render(request, 'recipes/edit_recipe.html', {'form':form})


@login_required
def delete_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        if recipe.owner != request.user:
            return redirect('recipes:index')
        recipe.delete()
        return redirect("recipes:index")
    
    return render(request, 'recipes/delete.html')


def save_and_redirect_recipe(form, request):
    recipe = form.save()
    recipe.string_to_ingredients(request.user)
    recipe.owner = request.user
    recipe.save()
    return redirect('recipes:detail', recipe_id=recipe.id)


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
    return render(request, 'recipes/ingredients_index.html', context)

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
    return render(request, 'recipes/ingredients_index.html', context)

@login_required
def ingredient_detail(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    recipes = ingredient.ingredient_uses.filter(owner = request.user)
    context = {'ingredient': ingredient, 'recipes': recipes}
    return render(request, 'recipes/ingredient_detail.html', context)

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
    return render(request, 'recipes/meal_plan_index.html', context)

@login_required
def meal_plan_detail(request, meal_plan_id):
    meal_plan = get_object_or_404(MealPlan, id=meal_plan_id, owner=request.user)
    recipe_list = list(meal_plan.recipes.all())
    ingredient_list = list(meal_plan.ingredients.all())
    context = {'meal_plan': meal_plan, 'recipe_list':recipe_list, 'ingredient_list': ingredient_list}
    return render(request, 'recipes/meal_plan_detail.html', context)

@login_required
def add_meal_plan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            mealplan = form.save(commit=False)
            mealplan.owner = request.user
            mealplan.save()
            form.save_m2m()
            return redirect('recipes:meal_plan_index')
    else:
        form = MealPlanForm()
    mealplans = MealPlan.objects.filter(owner=request.user)
    return render(request, 'recipes/add_meal_plan.html', {'mealplans': mealplans, 'form': form})

@login_required
def edit_meal_plan(request, id):
    #TODO: Break up the ingredients lists by the recipe they go in
    meal_plan = get_object_or_404(MealPlan, id=id, owner=request.user)

    if request.method == 'POST':
        selected_ingredients = request.POST.getlist('ingredients')
        meal_plan.ingredients.set(selected_ingredients)
        meal_plan.save()
        ingredients_owned = set(ingredient for recipe in meal_plan.recipes.all() for ingredient in recipe.uses_ingredient.exclude(id__in=meal_plan.ingredients.all()) )
        profile = request.user.profile
        profile.ingredients_owned.add(*ingredients_owned)
        profile.save()
        return redirect('recipes:meal_plan_detail', meal_plan_id=id)
    
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
    return render(request, 'recipes/edit_meal_plan.html', context)