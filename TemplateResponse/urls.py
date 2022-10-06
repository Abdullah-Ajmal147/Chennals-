from django.urls import path, include

from  TemplateResponse import views

urlpatterns = [
    path('', views.create_template)
]