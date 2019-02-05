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
        
        
        admission_number = forms.CharField(required=True , max_length=8)

        class Meta:
            model = Participate
            fields = (
            'event',
            )
