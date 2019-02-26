from django.db import models




class Student(models.Model):
    admission_number = models.CharField(max_length = 8)
    name = models.CharField(max_length=100)
    passout_year = models.IntegerField(null = True , blank = True)



class DutyLeave(models.Model):
    student = models.ForeignKey('Student' , on_delete=models.CASCADE)
    date = models.DateField()
    year = models.ForeignKey('sportsbackend.Year' , on_delete=models.CASCADE)
    hour = models.CharField(max_length=100 )
    reason = models.TextField()
    is_approved = models.BooleanField(default = False)


class ChestNo(models.Model):
    student = models.ForeignKey('Student' , on_delete=models.CASCADE)
    year = models.ForeignKey('sportsbackend.Year' , on_delete=models.CASCADE)
    cno = models.IntegerField()
