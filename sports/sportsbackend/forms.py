from django import forms

from .models import Event,Participate

from django.core.validators import MaxLengthValidator

from django.contrib.auth.forms import AuthenticationForm


class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
        'event_name',
        )

    def __init__(self, *args, **kwargs):
        super(EventCreateForm, self).__init__(*args, **kwargs)
        self.fields['event_name'].widget.attrs.update({
                'class': 'form-control',
            })


class ParticipationForm(forms.ModelForm):
        
        
        admission_number = forms.CharField(required=True , max_length=8)

        class Meta:
            model = Participate
            fields = (
            'event',

            )
        def __init__(self, *args, **kwargs):
            super(ParticipationForm, self).__init__(*args, **kwargs)
            self.fields['event'].widget.attrs.update({
                    'class': 'form-control',
                })
            self.fields['admission_number'].widget.attrs.update({
                    'class': 'form-control',
                })

class EventSelectForm(forms.ModelForm):


    class Meta:
        model = Participate
        fields = (
        'event',
        )

    def __init__(self, *args, **kwargs):
        super(EventSelectForm, self).__init__(*args, **kwargs)
        self.fields['event'].widget.attrs.update({
                'class': 'form-control',
            })

class AdmissionNumberForm(forms.ModelForm):


        class Meta:
            model = Participate
            fields = (
            'pos',

            )
        admission_number = forms.CharField(required=True , max_length=8)

        
        def __init__(self, *args, **kwargs):
            super(AdmissionNumberForm, self).__init__(*args, **kwargs)
            self.fields['pos'].widget.attrs.update({
                    'class': 'form-control',
                })
            self.fields['admission_number'].widget.attrs.update({
                    'class': 'form-control',
                })


class YearSelectForm(forms.Form):


        year = forms.CharField(max_length=4)
        
        def __init__(self, *args, **kwargs):
            super(YearSelectForm, self).__init__(*args, **kwargs)
            self.fields['year'].widget.attrs.update({
                    'class': 'form-control',
                })


class StudentReportForm(forms.Form):



        admission_number = forms.CharField(required=True , max_length=8)
        report_year = forms.IntegerField(required=False )
        
        def __init__(self, *args, **kwargs):
            super(StudentReportForm, self).__init__(*args, **kwargs)
            self.fields['admission_number'].widget.attrs.update({
                    'class': 'form-control',
                })
            self.fields['report_year'].widget.attrs.update({
                    'class': 'form-control',
                })
