# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.forms import HomeForm
from home.models import Post, Friend


class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all().order_by('-created')
		users = User.objects.exclude(id=request.user.id)
		
		args = {'form': form, 'posts': posts, 'users': users}
		return render(request, self.template_name, args)

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']
			form = HomeForm()
			return redirect('home:home')
		
		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)

def change_friends(request, operation, pk):
	new_friend = User.objects.get(pk=pk)
	if operation == 'add':
		Friend.make_friend(request.user, new_friend)
	elif operation == 'remove':
		Friend.lose_friend(request.user, new_friend)
	return redirect('home:home')
