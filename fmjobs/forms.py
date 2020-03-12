# -*- coding: utf-8 -*-
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'link1title', 'link1', 'link2title', 'link2', 'link3title', 'link3', 'link4title', 'link4', 'link5title', 'link5', 'text', 'monthlyincome', 'profitperiod', 'advantage', 'weakness',)
