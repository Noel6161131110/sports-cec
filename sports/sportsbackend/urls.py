

from django.urls import path, include

from django.contrib.auth import views as auth_views

from .views import AddEvent,CreateParticipation,ConfirmParticipationSelect,StudentReport,Disqualify,EventReport
from django.conf.urls.static import static

urlpatterns = [

path('addevent/', AddEvent.as_view(), name='addevent'),
path('addparticiapation/', CreateParticipation.as_view(), name='addparticipation'),
path('verifyparticiapation/', ConfirmParticipationSelect.as_view(), name='verifyparticipation'),
path('studentreport/', StudentReport.as_view(), name='studentreport'),
path('disqualify/', Disqualify.as_view(), name='disqualify'),
path('eventreport/', EventReport.as_view(), name='eventreport'),



]


