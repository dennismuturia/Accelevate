from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class userForms(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254, help_text='Required. Inform a valid email address.')
    firstName = forms.CharField(label="First Name")
    lastName = forms.CharField(label="Last Name")
    class meta:
        model = User
        fields = ['username', 'email', 'firstName', 'lastname', 'password1', 'password2']

    #Validation of passwords
    '''
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password']
    '''