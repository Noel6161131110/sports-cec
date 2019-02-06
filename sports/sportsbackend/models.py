from django.db import models

PARTICIPATION_CHOICES = (
(0,'Registered'),
(1,'First'),
(2,'Second'),
(3,'Third'),
(4,'Fourth'),
(5,'Participated'),
(6,'University'),
(7,'District'),
(8,'State'),
(9,'National'),
(10,'International'),
)

class Event(models.Model):
    event_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.event_name


class Year(models.Model):
    year = models.IntegerField()
    selected = models.BooleanField(default=False)
    def __str__(self):
        return str(self.year)

class Participate(models.Model):
    student = models.ForeignKey('student.Student' , on_delete=models.CASCADE)
    event = models.ForeignKey("Event" , on_delete=models.CASCADE)
    year = models.ForeignKey("Year" , on_delete=models.CASCADE)
    position = models.IntegerField( choices=PARTICIPATION_CHOICES, default=0)
