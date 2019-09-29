# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from home.forms import HomeForm



class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self, request):
		form = HomeForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['post']
			form = HomeForm()
			return redirect('home:home')
		
		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)
