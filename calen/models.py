from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Vacation(models.Model):
    EmpName=models.CharField(max_length=100)
    EmpId=models.CharField(max_length=30)
    vacationStartdate=models.DateTimeField()
    vacationEnddate=models.DateTimeField()
