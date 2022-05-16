from django import urls
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import EmployeeView


urlpatterns = [
    
 
 path('employee/', EmployeeView.as_view({'get': 'list', 'post':'create'}) , name="employee"),
 path('employee/<int:pk>/', EmployeeView.as_view({'get': 'retrieve', 'put':'update','delete':'destroy'}) , name="employee"),
 
    
]
