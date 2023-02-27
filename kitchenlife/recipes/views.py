from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from kitchenlife.openai_link import sendPrompt
from .models import Recipe
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
    method_as_list = recipe.method_as_list()
    try:
        dumb_ingredients = recipe.ingredients_string.split('\n')
        ingredients = list(recipe.uses_ingredient.all())
        combined_ingredients = []
        for dumb_ingredient in dumb_ingredients:
            for ingredient in ingredients:
                if ingredient.name.lower() in dumb_ingredient.lower():
                    combined_ingredients.append((dumb_ingredient, ingredient))
                    break
    except:
        combined_ingredients = None
    
    print(recipe.ingredients_string)
                
    context = {'recipe': recipe, 'method_as_list': method_as_list, 'combined_ingredients': combined_ingredients}
    return render(request, 'recipes/detail.html', context)


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['img'])
            text = new_recipe_processing.image_to_string(img, active_user = request.user.profile)
            recipe = new_recipe_processing.text_to_recipe(text)
            recipe.save()
            recipe.owner = request.user
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
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.owner != request.user:
        return redirect('recipes:index')
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance= recipe)
        if form.is_valid():
            form.save()
            if not recipe.simplified_ingredients:
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