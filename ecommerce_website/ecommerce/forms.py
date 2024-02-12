from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(label='User')
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Confirm', widget = forms.PasswordInput)

