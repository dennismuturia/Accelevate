from django.contrib.auth.models import User
from django import forms
from wtforms import ValidationError


class userForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')
    email = forms.EmailField(label='Email')
    firstName = forms.CharField(label="First Name")
    lastName = forms.CharField(label="Last Name")
    class meta:
        model = User
        fields = ['username', 'email']

    #Validation of passwords
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password']