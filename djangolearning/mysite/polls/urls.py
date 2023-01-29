# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:41:35 2023

@author: Charl
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]