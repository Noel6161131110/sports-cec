from django.db import models

# Create your models here.

class Student(models.Model)
    admission_number = models.CharField(max_length = 8)
    name = models.CharField(max_length=100)
    passout_year = models.IntegerField()
    phonenumber = models.IntegerField()
    address = models.TextField()
    
