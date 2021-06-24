from django import forms

from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [

        ]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)