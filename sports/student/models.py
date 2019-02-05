from django.db import models

# Create your models here.

class Student(models.Model):
    admission_number = models.CharField(max_length = 8)
    name = models.CharField(max_length=100)
    passout_year = models.IntegerField(null = True , blank = True)
    phonenumber = models.IntegerField(null = True , blank = True)
    address = models.TextField(null = True , blank = True)
