
from django.urls import path, include

from .views import StudentAdd, UploadCSV, CNo , AddDutyLeave , DutyLeaveList , DutyLeaveConfirm , DutyLeaveReport

urlpatterns = [

path('addstudent/', StudentAdd.as_view(), name='addstudent'),
path('cno/', CNo.as_view(), name='CNO'),
path('uploadcsv/', UploadCSV.as_view(), name='bulkadd'),
path('dutyleaveadd/', AddDutyLeave.as_view(), name='addduty'),
path('dutyleavelist/', DutyLeaveList.as_view(), name='dutyleavelist'),
path('dutyleaveconfirm/', DutyLeaveConfirm.as_view(), name='dutyleaveconfirm'),
path('dutyleavereport/', DutyLeaveReport.as_view(), name='dutyleavereport'),


]
