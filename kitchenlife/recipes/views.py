from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from re import split as resplit
from re import findall as refindall

from kitchenlife.openai_link import sendPrompt, sendPromptIngredients
from .models import Recipe, RecipeIngredient
from .forms import QuantityForm, UploadFileForm, EditRecipeForm, SearchForm, UploadURLForm, EditIngredientsForm
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
    # recipe.simplified_to_ingredients(request.user)
    if request.method == 'POST':
        form = form = QuantityForm(request.POST)
        if form.is_valid():
            scale = int(form.cleaned_data['serving'])/recipe.serves_int
    else:
        form = QuantityForm()
        scale = 1
    method_as_list = recipe.method_as_list()
    nutrients = recipe.return_nutritional_info()
    #print(nutrients)
    context = {'recipe': recipe, 'method_as_list': method_as_list, 'scale': scale, 'form': form, 'nutrients': nutrients}
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

def generate_recipe_suggestion(request):
    ingredients = ", ".join(request.user.profile.ingredients_owned_list())
    myprompt = ("Provide 5 varied recipe briefs that use any combination of these ingredients:\n\n\n "+
                ingredients)
    
    response = sendPrompt(myprompt, request.user.profile, temperature=0.5)
    print(response)
    return redirect("recipes:index")