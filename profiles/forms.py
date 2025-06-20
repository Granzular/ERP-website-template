from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length='150')
    password = forms.CharField(max_length='25',widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username","email","password"]
        widgets = {
                'password':forms.PasswordInput,
                }

