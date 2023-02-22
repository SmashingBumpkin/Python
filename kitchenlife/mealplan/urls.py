from django.urls import path

from . import views

app_name = 'mealplan'
urlpatterns = [
    path('', views.meal_plan_index, name='meal_plan_index'),
    path('addmealplan/', views.add_meal_plan, name='add_meal_plan'),
    path('mealplandetail/<int:meal_plan_id>/', views.meal_plan_detail, name='meal_plan_detail'),
    path('<int:id>/edit/', views.edit_meal_plan, name='edit_meal_plan'),
]