from django.contrib.auth.models import User
from django import forms

class userForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    email = forms.EmailField(label='Email')
    firstName = forms.CharField(label="First Name")
    lastName = forms.CharField(label="Last Name")