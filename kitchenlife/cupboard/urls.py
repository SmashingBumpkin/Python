from django.urls import path

from . import views

app_name = 'cupboard'
urlpatterns = [
    path('', views.ingredients_index, name='ingredients_index'),
    path('ingredients/<int:ingredient_id>/', views.ingredient_detail, name='ingredient_detail'),
    path('cupboard/', views.cupboard_index, name='cupboard_index'),
    path('editcupboard/', views.edit_cupboard, name='edit_cupboard'),
]