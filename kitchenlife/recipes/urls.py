from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('ingredients/', views.ingredients_index, name='ingredients_index'),
    path('ingredients/<int:ingredient_id>/', views.ingredient_detail, name='ingredient_detail'),
    path('view/<int:recipe_id>/', views.detail, name='detail'),
    path('upload_photo/', views.upload_file, name='upload_photo'),
    path('upload_url/', views.upload_url, name='upload_url'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name= 'edit_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name= 'delete_recipe'),
]