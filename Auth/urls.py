from django.contrib import admin
from django.urls import path, include
from Auth import views

urlpatterns = [
    
    path('signup/',views.signup)
    
]