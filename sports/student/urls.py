
from django.urls import path, include

from .views import StudentAdd, UploadCSV, CNo

urlpatterns = [

path('addstudent/', StudentAdd.as_view(), name='addstudent'),
path('cno/', CNo.as_view(), name='CNO'),
path('uploadcsv/', UploadCSV.as_view(), name='bulkadd'),


]
