

from django.urls import path, include
from django.conf import settings

from .views import AddEvent,CreateParticipation,ConfirmParticipationSelect,StudentReport
from django.conf.urls.static import static

urlpatterns = [

path('addevent/', AddEvent.as_view(), name='addevent'),
path('addparticiapation/', CreateParticipation.as_view(), name='addparticipation'),
path('verifyparticiapation/', ConfirmParticipationSelect.as_view(), name='verifyparticipation'),
path('studentreport/', StudentReport.as_view(), name='studentreport'),

]


