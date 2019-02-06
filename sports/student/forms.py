from django import forms

from .models import Student

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

