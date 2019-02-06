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

class EventSelectForm(forms.ModelForm):


    class Meta:
        model = Participate
        fields = (
        'event',
        )

class AdmissionNumberForm(forms.ModelForm):

        admission_number = forms.CharField(required=True , max_length=8)

        class Meta:
            model = Participate
            fields = (
            'position',

            )
        
        def __init__(self, *args, **kwargs):
            super(AdmissionNumberForm, self).__init__(*args, **kwargs)
            self.fields['position'].widget.attrs.update({
                    'class': 'form-control',
                })
            self.fields['admission_number'].widget.attrs.update({
                    'class': 'form-control',
                })
        