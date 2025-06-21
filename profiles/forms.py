from .models import CustomUser
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=25,widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    public_key = forms.CharField(max_length=9)
    class Meta:
        model = CustomUser
        fields = ["username","email","user_type","password"]
        widgets = {
                'password':forms.PasswordInput,
                'user_type':forms.RadioSelect,
                }

    def clean_public_key(self):
        data = self.cleaned_data['public_key']
        if not data and self.cleaned_data['user_type']=='staff':
            raise forms.ValidationError("this field is required")
        return data

