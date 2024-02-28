from django import forms
from .models import Profile

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Confirm', widget = forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget = forms.PasswordInput)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            "image": "Choose a image"
        }
