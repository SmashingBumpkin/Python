from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from re import split as resplit
from re import findall as refindall

from kitchenlife.openai_link import sendPrompt, sendPromptIngredients
from .models import Recipe, RecipeIngredient
from .forms import UploadFileForm, EditRecipeForm, SearchForm, UploadURLForm, EditIngredientsForm
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
        if not recipe_list:
            print("hi")
    context = {'recipe_list': recipe_list, 'form': form}
    return render(request, 'recipes/index.html', context)


@login_required
def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.owner != request.user:
        return redirect('recipes:index')
    # recipe.simplified_to_ingredients(request.user)
    method_as_list = recipe.method_as_list()
    context = {'recipe': recipe, 'method_as_list': method_as_list}
    return render(request, 'recipes/detail.html', context)


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['img'])
            recipe = new_recipe_processing.image_to_recipe(img, user = request.user)
            recipe.save()
            # recipe.from_photo = True
            # recipe.owner = request.user
            # recipe.save()
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
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.owner != request.user:
        return redirect('recipes:index')
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance= recipe)
        if form.is_valid():
            new_ingr_str = form.cleaned_data['ingredients_string'].strip()
            old_ingred_str = recipe.simplified_ingredients
            form.save()
            if old_ingred_str != new_ingr_str: 
                recipe.recipe_ingredient.all().delete()
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
            form.save()
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

def generate_recipe_suggestion(request):
    ingredients = ", ".join(request.user.profile.ingredients_owned_list())
    myprompt = ("Provide 5 varied recipe briefs that use any combination of these ingredients:\n\n\n "+
                ingredients)
    
    response = sendPrompt(myprompt, request.user.profile, temperature=0.5)
    print(response)
    return redirect("recipes:index")