from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Recipe
from .forms import UploadFileForm
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

def add_recipe(request):
    recipe_name = "test"
    recipe_method = "try to test"
    ingredients_string = "1 test"
    new_recipe = Recipe.objects.create(recipe_name = recipe_name, 
        recipe_method = recipe_method, ingredients_string = ingredients_string)
    return HttpResponse("Hello, world. You're at the add recipe page.")

def upload_file(request):
    if request.method == 'POST' and request.FILES:
        print("Helkoo")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['img'])
            
            text = image_processing.image_to_string(img)
            recipe = image_processing.text_to_recipe(text)
            return render(request, 'recipes/success.html', {'name': recipe.recipe_name, 
                                                            'ingredients': recipe.ingredients_string, 
                                                            'method': recipe.recipe_method}
                                                            )
    elif request.method == 'POST':
        print("hi")
        #Add recipe to database
        #return success page
        #go back to recipes home
    else:
        form = UploadFileForm()
    return render(request, 'recipes/upload.html', {'form': form})