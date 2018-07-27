# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.views.genetic import View
from .forms import userForms

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def signUp(request):
    
    return render(request, 'signup.html')
