# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.views.genetic import View
from django.views.generic import CreateView

from .forms import userForms

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')
'''
This is view for the user registration
'''
class RegisterUserView(CreateView):
    form_class = userForms
    template_name = 'signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponse('User Registred')

'''
def signUp(request):
    
    return render(request, 'signup.html')
'''