# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#In here is the data the user will enter
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    email = models.EmailField()
    school = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    '''
    #Update the student information
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    '''