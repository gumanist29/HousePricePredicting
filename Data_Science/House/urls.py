from django.contrib import admin
from django.urls import path
from .views import home_view, HomeList

urlpatterns = [
    path('home/', home_view, name='home_view'),
    path('api/', HomeList.as_view(), name='home_api'),
]