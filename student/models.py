from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    degree=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=15)


