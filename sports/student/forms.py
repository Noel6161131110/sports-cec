from django import forms

from .models import Student

from django.core.validators import MaxLengthValidator

class StudentCreationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = (
        'admission_number',
        'name',
        'passout_year',
        'phonenumber',
        'address'
        )


