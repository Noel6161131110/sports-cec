
from django.urls import path, include

from .views import StudentAdd, UploadCSV

urlpatterns = [

path('addstudent/', StudentAdd.as_view(), name='addstudent'),
path('uploadcsv/', UploadCSV.as_view(), name='bulkadd'),


]
