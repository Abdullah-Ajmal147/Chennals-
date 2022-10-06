from django.urls import path, include

from  MergePDf import views

urlpatterns = [
    path('mergedf/',views.merge),
    path('data_post/',views.data_post),
]