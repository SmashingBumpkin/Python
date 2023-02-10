from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Recipe, Ingredient
from .forms import CustomUserCreationForm, UploadFileForm, EditRecipeForm, SearchForm, UploadURLForm
from PIL import Image
# Imaginary function to handle an uploaded file.
from . import new_recipe_processing
from django.contrib.auth import login



def ingredients_index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            filtered_ingredient = form.cleaned_data['search_term']
            ingredient_list = Ingredient.objects.filter(ingredient_name__contains=filtered_ingredient).order_by("ingredient_name")
    else:
        form = SearchForm()
        ingredient_list = Ingredient.objects.all().order_by("ingredient_name")
    context = {'ingredient_list': ingredient_list, 'form': form}
    return render(request, 'recipes/ingredients_index.html', context)



def ingredient_detail(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    return render(request, 'recipes/ingredient_detail.html', {'ingredient': ingredient})



def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            filtered_recipe = form.cleaned_data['search_term']
            recipe_list = Recipe.objects.filter(name__contains=filtered_recipe).order_by("name")
    else:
        form = SearchForm()
        recipe_list = Recipe.objects.all().order_by("name")
    context = {'recipe_list': recipe_list, 'form': form}
    return render(request, 'recipes/index.html', context)



def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    method_as_list = recipe.method.split('\n')
    return render(request, 'recipes/detail.html', {'recipe': recipe, 'method_as_list': method_as_list})


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
        recipe = form.save()
        recipe.string_to_ingredients()
        return redirect('recipes:detail', recipe_id=recipe.id)
    else:
        form = UploadFileForm()

    return render(request, 'recipes/upload.html', {'form': form})

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
                recipe = editForm.save()
                recipe.string_to_ingredients()
                return redirect('recipes:detail', recipe_id=recipe.id)
            else:
                print("ERROR: Submitted form was invalid\n\n\n")
                print(editForm.errors)
                print("\n\n\n")

    form = UploadURLForm()
    return render(request, 'recipes/upload.html', {'form': form})

def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
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

def delete_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        recipe.delete()
        return redirect("recipes:index")
    return render(request, 'recipes/delete.html')
