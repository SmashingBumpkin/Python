from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from re import split as resplit
from re import findall as refindall

from kitchenlife.openai_link import sendPrompt, sendPromptIngredients
from .models import Profile, Recipe, RecipeIngredient
from .forms import PlaintextForm, QuantityForm, UploadFileForm, EditRecipeForm, SearchForm, UploadURLForm, EditIngredientsForm
from PIL import Image
from . import new_recipe_processing


@login_required
def index(request):
    if request.method == 'POST' and "filter_by_search" in request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            filtered_recipe = form.cleaned_data['search_term']
            recipe_list = Recipe.objects.filter(name__contains=filtered_recipe, owner=request.user).order_by("name")
    elif request.method == 'POST' and "sort_by_match" in request.POST:
        form = SearchForm()
        recipe_list = Recipe.objects.filter(owner=request.user)
        profile = request.user.profile
        profile_ingredient_set = set(profile.profile_ingredient.filter(in_stock = True).values_list('id', flat=True))
        recipes_with_match_data = []
        for recipe in recipe_list:
            recipe_ingredient_set = set(recipe.recipe_ingredient.all().values_list('profile_ingredient', flat=True))
            num_recipe_ingredients = len(recipe_ingredient_set)
            recipe_ingredient_set.difference_update(recipe_ingredient_set- profile_ingredient_set)
            try:
                number_present = len(recipe_ingredient_set)
            except:
                number_present = 0
            percentage_owned = int((number_present/num_recipe_ingredients)*100)
            recipes_with_match_data.append((recipe, num_recipe_ingredients-number_present, percentage_owned))
        recipes_with_match_data.sort(key=lambda x: x[2], reverse=True)
        context = {'recipes_with_match_data': recipes_with_match_data, 'form': form}
        return render(request, 'recipes/index.html', context)
            
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
    # recipe.simplified_to_ingredients(request.user)
    formServing = QuantityForm()
    formNutrition = QuantityForm()
    scale = 1
    scale_nutrition = 1
    if request.method == 'POST':
        if "scale_quantities" in request.POST:
            formServing = QuantityForm(request.POST)
            if formServing.is_valid():
                scale = int(formServing.cleaned_data['serving'])/recipe.serves_int
        elif "scale_nutrition" in request.POST:
            formNutrition = QuantityForm(request.POST)
            if formNutrition.is_valid():
                scale_nutrition = int(formNutrition.cleaned_data['serving'])/100
        elif "add_all_ingredients" in request.POST:
            profile = request.user.profile
            profile.add_items_from_recipe(recipe)
    method_as_list = recipe.method_as_list()
    nutrients = recipe.return_nutritional_info(scale_nutrition)
    #print(nutrients)
    context = {'recipe': recipe, 
               'method_as_list': method_as_list, 
               'scale': scale, 
               'formServing': formServing,
               'formNutrition': formNutrition, 
               'nutrients': nutrients}
    return render(request, 'recipes/detail.html', context)

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['img'])
            recipe = new_recipe_processing.image_to_recipe(img, user = request.user)
            recipe.save()
            return redirect('recipes:edit_recipe', recipe_id = recipe.id)

    form = UploadFileForm()

    return render(request, 'recipes/upload.html', {'form': form})


@login_required
def upload_url(request):
    if request.method == 'POST':
        uploadForm = UploadURLForm(request.POST.copy())
        if uploadForm.is_valid():
            filtered_url = uploadForm.cleaned_data['uploadedurl']
            recipe = new_recipe_processing.url_to_recipe(filtered_url, request.user)
            recipe.save()
            return redirect('recipes:edit_recipe', recipe_id = recipe.id)

    form = UploadURLForm()
    return render(request, 'recipes/upload.html', {'form': form})

@login_required
def upload_text(request):
    if request.method == 'POST':
        uploadForm = PlaintextForm(request.POST.copy())
        if uploadForm.is_valid():
            text = uploadForm.cleaned_data['text']
            recipe = new_recipe_processing.text_to_recipe(text, request.user)
            recipe.save()
            return redirect('recipes:edit_recipe', recipe_id = recipe.id)

    form = PlaintextForm()
    return render(request, 'recipes/upload.html', {'form': form})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.owner != request.user:
        return redirect('recipes:index')
    if request.method == 'POST':
        old_ingred_str = recipe.ingredients_string.strip()
        form = EditRecipeForm(request.POST, instance= recipe)
        if form.is_valid():
            new_ingred_str = form.cleaned_data['ingredients_string'].strip()
            form.save()
            recipe.serves_to_int()
            recipe.save()
            if old_ingred_str != new_ingred_str:
                #recipe.recipe_ingredient.all().delete()
                recipe.simplify_ingredients(request.user)
                recipe.save()
            return redirect('recipes:edit_ingredients', recipe_id=recipe.id)
    form = EditRecipeForm(initial = recipe.return_dict())
    return render(request, 'recipes/edit_recipe.html', {'form':form})

@login_required
def edit_ingredients(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.owner != request.user:
        return redirect('recipes:index')
    if request.method == 'POST':
        form = EditIngredientsForm(request.POST, instance=recipe)
        if form.is_valid():
            # new_ingr_str = form.cleaned_data['simplified_ingredients'].strip()
            # old_ingred_str = recipe.simplified_ingredients
            form.save()
            #if old_ingred_str != new_ingr_str: 
            recipe.simplified_to_ingredients(request.user)
            recipe.save()
            return redirect('recipes:detail', recipe_id=recipe.id)
    else:
        form = EditIngredientsForm(instance=recipe)
    return render(request, 'recipes/edit_ingredients.html', {'recipe': recipe, 'form': form})


@login_required
def delete_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        if recipe.owner != request.user:
            return redirect('recipes:index')
        recipe.delete()
        return redirect("recipes:index")
    
    return render(request, 'recipes/delete.html')

@login_required
def generate_recipe_suggestion(request):
    ingredients = request.user.profile.in_stock_string()
    #ingredients = ", ".join(ingredients_list)
    myprompt = ("Provide 5 varied recipe briefs that use any combination of these ingredients:\n\n\n "
                + ingredients)
    
    #response = sendPrompt(myprompt, request.user.profile, temperature=0.5)
    responses = """1. Spicy Chickpea Curry: A comforting, warming curry with a kick of heat. Made with garlic, cumin, turmeric, chilli powder, chopped tomatoes, chickpeas, coconut milk, vegetable oil, pumpkin seeds and herbs. 
2. Lemon and Vanilla Cake: A light and fluffy cake with a zesty lemon flavour and a hint of vanilla. Made with butter, caster sugar, self-raising flour, egg yolk, vanilla extract, lemon juice and zest. 
3. Ginger and Coriander Chicken: A fragrant and flavourful dish with a hint of sweetness from the ginger. Made with chicken, ginger, coriander, garlic, light brown soft sugar, vegetable oil and black pepper. 
4. Chocolate Chip and Pecorino Cookies: A sweet and savoury cookie with a hint of saltiness from the cheese. Made with butter, caster sugar, self-raising flour, egg yolk, chocolate chips, pecorino cheese and a pinch of salt. 
5. Pumpkin and Herb Risotto: A creamy, comforting risotto with a hint of sweetness from the pumpkin and freshness from the herbs. Made with vegetable oil, garlic, pumpkin, herbs, risotto rice, vegetable stock and pecorino cheese."""
    responses = responses.split('\n')
    print(responses)
    context = {'responses':responses}
    return render(request, 'recipes/view_generated_recipes.html', context)