# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from home.models import Post


class HomeForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'Write a post',
		}
	))

	class Meta:
		model = Post
		fields = ('post',)
