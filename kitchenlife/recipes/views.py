from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe
from .forms import UploadFileForm, EditRecipeForm
from PIL import Image
# Imaginary function to handle an uploaded file.
from . import image_processing

def index(request):
    recipe_list = Recipe.objects.all()
    template = loader.get_template('recipes/index.html')
    context = {'recipe_list': recipe_list}
    return render(request, 'recipes/index.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def upload_file(request):
    if request.method == 'POST' and request.FILES:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['img'])
            
            text = image_processing.image_to_string(img)
            recipe = image_processing.text_to_recipe(text)
            form = EditRecipeForm(initial = {
                        'name': recipe.name,
                        'method':recipe.method,
                        'serves':recipe.serves,
                        'description':recipe.description,
                        'book':recipe.book,
                        'page':recipe.page,
                        'ingredients_string':recipe.ingredients_string,
                        'method':recipe.method,
                    })
            return render(request, "recipes/edit_recipe.html", {"form": form})
    elif request.method == 'POST':
        form = EditRecipeForm(request.POST)
        recipe = form.save()
        return redirect("recipes:index")
    else:
        form = UploadFileForm()
    return render(request, 'recipes/upload.html', {'form': form})

def edit_recipe(request):
    if request.method == 'POST' and request.FILES:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['img'])
            
            text = image_processing.image_to_string(img)
            recipe = image_processing.text_to_recipe(text)
            form = EditRecipeForm(initial = {
                        'name': recipe.name,
                        'method':recipe.method,
                        'serves':recipe.serves,
                        'description':recipe.description,
                        'book':recipe.book,
                        'page':recipe.page,
                        'ingredients_string':recipe.ingredients_string,
                        'method':recipe.method,
                    })
            return render(request, "recipes/edit_recipe.html", {"form": form})
    elif request.method == 'POST':
        form = EditRecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect("recipes:index")