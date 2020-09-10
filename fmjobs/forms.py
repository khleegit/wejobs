# -*- coding: utf-8 -*-
from django import forms

from .models import Post, Classifications, Categorys

#from .models import Plan

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'link1title', 'link1', 'link2title', 'link2', 'link3title', 'link3', 'link4title', 'link4', 'link5title', 'link5', 'text', 'monthlyincome', 'profitperiod', 'advantage', 'weakness',)
        
        widgets = {
                    'title' : forms.TextInput(attrs = {'class': 'page-header'}),
                }

class classificationSaveForm(forms.ModelForm):
    
    class Meta:
        model = Classifications
        fields = ('classification',)
        
        widgets = {
                'classification' : forms.TextInput(attrs = {'class':'form-control col-12'}),
                }
        
        labels = {
                'classification' : "분류",
                }
        


class CategorySaveForm(forms.ModelForm):
    
    class Meta:
        model = Categorys
        fields = '__all__'
        
        widgets = {
                    'classification' : forms.Select(attrs = {'class': 'form-control col-12'}),
                    'category' : forms.TextInput(attrs = {'class': 'form-control col-12', 'placeholder' : '항목을 입력하세요'}),
                }
        

    


'''
class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('planer', 'classification', 'category', 'target_value', 'unit')
'''
        
        
'''        
https://www.youtube.com/watch?v=6-XXvUENY_8        
class ClassificationsForm(forms.ModelForm):
    class Meta:
        model = Classifications
        field = ('', 'classification')
'''