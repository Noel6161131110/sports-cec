from django import forms

from .models import Event,Participate

from django.core.validators import MaxLengthValidator

class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
        'event_name',
        )

class ParticipationForm(forms.ModelForm):
        
        
        
        class Meta:
            model = Participate
            fields = (
            'event',
            )
