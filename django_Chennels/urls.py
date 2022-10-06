from django.contrib import admin
from django.urls import path, include
from django_Chennels import views

urlpatterns = [
    path('chat/', views.chat ),
    path('<str:room_name>/', views.room, name='room'),
]
