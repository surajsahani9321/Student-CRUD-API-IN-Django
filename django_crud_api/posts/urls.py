from django import urls
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import  PostView


urlpatterns = [
    
 
 path('posts/', PostView.as_view({'get': 'list', 'post':'create'}) , name="posts"),
 path('posts/<int:pk>/', PostView.as_view({'get': 'retrieve', 'put':'update','delete':'destroy'}) , name="posts"),
 
    
]
