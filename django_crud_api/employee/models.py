from django.db import models


class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    designation=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)