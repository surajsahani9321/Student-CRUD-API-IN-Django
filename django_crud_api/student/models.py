from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)