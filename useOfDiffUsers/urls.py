from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/', views.saveit, name='saveit'),
    path('', views.session__delete, name="delete_session")
]