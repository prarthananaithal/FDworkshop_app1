# app1/urls.py
from django.urls import path
from app1.views import substring_view

urlpatterns = [
    #path('', substring_view),  # Route for the root URL
    path('', substring_view, name='substring_combinations'),# Add other paths for your app here
]