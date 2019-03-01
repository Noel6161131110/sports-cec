from django import forms

from .models import Student, ChestNo , DutyLeave

from django.core.validators import MaxLengthValidator

class StudentCreationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = (
        'admission_number',
        'name',
        )

    def __init__(self, *args, **kwargs):
        super(StudentCreationForm, self).__init__(*args, **kwargs)
        self.fields['admission_number'].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['name'].widget.attrs.update({
                'class': 'form-control',
            })


class ChestNumberUpdation(forms.ModelForm):

    admission_number = forms.CharField(max_length=8)
    
    class Meta:
        model = ChestNo
        fields = (
        'cno',
        )

    def __init__(self, *args, **kwargs):
        super(ChestNumberUpdation, self).__init__(*args, **kwargs)
        self.fields['admission_number'].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['cno'].widget.attrs.update({
                'class': 'form-control',
            })



class DutyLeaveForm(forms.ModelForm):



        admission_number = forms.CharField(required=True , max_length=8)
        
        class Meta:
            model = DutyLeave
            fields = (
            'date',
            'hour',
            'reason',
            )
        
        def __init__(self, *args, **kwargs):
            super(DutyLeaveForm, self).__init__(*args, **kwargs)
            self.fields['admission_number'].widget.attrs.update({
                    'class': 'form-control',
                })
            self.fields['date'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : "Enter Date as Month/Date/Year"
                })
            self.fields['hour'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : "Enter Comma Sperated Hours"
                })
            self.fields['reason'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : "Enter Reason For Duty Leave Application"
                })
                
                
class DateForm(forms.ModelForm):

        datefrom = forms.DateField()
        dateto = forms.DateField()
        admission_number = forms.CharField(required=False , max_length=8)

        class Meta:
            model = DutyLeave
            fields = (
            )
        
        def __init__(self, *args, **kwargs):
            super(DateForm, self).__init__(*args, **kwargs)
            self.fields['datefrom'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : "Enter Starting Date as Month/Date/Year"
                })
            self.fields['dateto'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : "Enter Ending Date as Month/Date/Year"
                })
            self.fields['admission_number'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : "Enter Admission Number for Induvidual Reports"
                })

                
                    
