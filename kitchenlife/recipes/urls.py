from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('upload/', views.upload_file, name='upload'),
    path('edit/', views.edit_recipe, name= 'edit_recipe')
]