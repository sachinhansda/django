# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfileManager(models.Manager):
	def get_queryset(self):
		return super(UserProfileManager, self).get_queryset().filter(city='Palakkad')

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	decription = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	phone = models.IntegerField(default=0)
	image = models.ImageField(upload_to='profile_image', blank=True)

	palakkad = UserProfileManager()

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
