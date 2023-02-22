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
    path('cupboard/', views.cupboard_index, name='cupboard_index'),
    path('mealplans/', views.meal_plan_index, name='meal_plan_index'),
    path('addmealplan/', views.add_meal_plan, name='add_meal_plan'),
    path('mealplandetail/<int:meal_plan_id>/', views.meal_plan_detail, name='meal_plan_detail'),
    path('mealplans/<int:id>/edit/', views.edit_meal_plan, name='edit_meal_plan'),
]