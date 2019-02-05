from django.db import models


class Student(models.Model):
    admission_number = models.CharField(max_length = 8)
    name = models.CharField(max_length=100)
    passout_year = models.IntegerField(null = True , blank = True)



class DutyLeave(models.Model):
    student = models.ForeignKey('Student' , on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.IntegerField()