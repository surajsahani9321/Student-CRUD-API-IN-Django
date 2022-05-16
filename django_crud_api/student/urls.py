from django import urls
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import StudentView


urlpatterns = [
    
 
 path('students/', StudentView.as_view({'get': 'list', 'post':'create'}) , name="students"),
 path('students/<int:pk>/',StudentView.as_view({'get': 'retrieve', 'put':'update','delete':'destroy'}) , name="students"),
 
    
]
