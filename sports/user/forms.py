from django import forms

from .models import User

from django.core.validators import MaxLengthValidator

class UserCreationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = (
        'first_name',
        'last_name',
        'username',
        'password',
        'email',
        )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
                'placeholder': 'First Name',
                'class': 'form-control',
            })
        self.fields['last_name'].widget.attrs.update({
                'placeholder': 'Last Name',
                'class': 'form-control',
            })
        self.fields['username'].widget.attrs.update({
                'placeholder': 'Username',
                'class': 'form-control',
            })

        self.fields['password'].widget.attrs.update({
                'placeholder': 'Password',
                'class': 'form-control',
            })
        self.fields['email'].widget.attrs.update({
                'placeholder': 'Email Address',
                'class': 'form-control',
            })


class UserLoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
        'username',
        'password',
        )


    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                'placeholder': 'Username',
                'class': 'form-control',
            })

        self.fields['password'].widget.attrs.update({
                'placeholder': 'Password',
                'class': 'form-control',
            })