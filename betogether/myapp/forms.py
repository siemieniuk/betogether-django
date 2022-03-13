from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')
    agreement = forms.CheckboxInput()

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)