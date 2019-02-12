from django import forms

from .models import Student, ChestNo

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

