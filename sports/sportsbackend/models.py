from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length = 50)

class Year(models.Model):
    year = models.IntegerField()

class Participate(models.Model):
    student = models.ForeignKey('student.Student' , on_delete=models.CASCADE)
    event = models.ForeignKey("Event" , on_delete=models.CASCADE)
    year = models.ForeignKey("Year" , on_delete=models.CASCADE)
    position = models.IntegerField(default=-1)
