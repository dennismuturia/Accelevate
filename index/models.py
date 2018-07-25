# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#In here is the data the user will enter
class student(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    email = models.EmailField()
    school = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class worker(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    email = models.EmailField()
    placeofwork = models.CharField(max_length=100)
    password = models.CharField(max_length=50)