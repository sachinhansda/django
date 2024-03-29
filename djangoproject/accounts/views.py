# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect 
from accounts.forms import (
	RegistrationForm,
	EditProfileForm	
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = RegistrationForm() 

		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)



def view_profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
	args = {'user': user}
	return render(request, 'accounts/profile.html', args)


def edit_profile(request):
	if request.method  == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/profile')

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile')
		else:
			return redirect('/account/change-password')
	else:
		form = PasswordChangeForm(user=request.user)

		args = {'form': form}
		return render(request, 'accounts/change_password.html', args)
