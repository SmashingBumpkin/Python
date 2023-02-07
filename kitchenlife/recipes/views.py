from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe, Ingredient
from .forms import UploadFileForm, EditRecipeForm
from PIL import Image
# Imaginary function to handle an uploaded file.
from . import image_processing

def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}
    return render(request, 'recipes/index.html', context)

def ingredients_index(request):
    ingredient_list = Ingredient.objects.all().order_by("ingredient_name")
    context = {'ingredient_list': ingredient_list}
    return render(request, 'recipes/ingredients_index.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.string_to_ingredients()
    method_as_list = recipe.method.split('\n')
    return render(request, 'recipes/detail.html', {'recipe': recipe, 'method_as_list': method_as_list})

def ingredient_detail(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    return render(request, 'recipes/ingredient_detail.html', {'ingredient': ingredient})



def upload_file(request):
    if request.method == 'POST' and request.FILES:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['img'])
            text = image_processing.image_to_string(img)
            recipe = image_processing.text_to_recipe(text)
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