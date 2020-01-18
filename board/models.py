from django.db import models

# Create your models here.
class Employee(models.Model):
    EmpName=models.CharField(max_length=100)
    EmpId=models.CharField(max_length=30,primary_key=True)
