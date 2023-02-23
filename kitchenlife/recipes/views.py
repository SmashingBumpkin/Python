from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Recipe
from .forms import UploadFileForm, EditRecipeForm, SearchForm, UploadURLForm
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
    print(request.POST)
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