from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:recipe_id>/', views.detail, name='detail'),
    path('nutrition/<int:recipe_id>/', views.nutrition_detail, name='nutrition_detail'),
    path('upload_photo/', views.upload_file, name='upload_photo'),
    path('upload_url/', views.upload_url, name='upload_url'),
    path('upload_text/', views.upload_text, name='upload_text'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name= 'edit_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name= 'delete_recipe'),
    path('edit_ingredients/<int:recipe_id>/', views.edit_ingredients, name= 'edit_ingredients'),
    path('generate_recipe_suggestion/', views.generate_recipe_suggestion, name= 'generate_recipe_suggestion'),
]