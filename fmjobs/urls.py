# -*- coding: utf-8 -*-

from django.urls import path
from . import views



urlpatterns = [
#    path('', views.post_blank, name='post_blank'),
    path('', views.login, name='login'),
    path('post/list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('weplan', views.weplan, name='weplan'),
    path('weplan/dashboard', views.dashboard, name='dashboard'),
    path('weplan/targetregistration', views.targetregistration, name='targetregistration'),
    path('weplan/targetsetting', views.targetsetting, name='targetsetting'),
    path('weplan/classification', views.classification, name='classification'),
    path('weplan/classification/classification_new', views.classification_new, name = 'classification_new'),
    path('weplan/classification/classification_edit/<int:pk>/', views.classification_edit, name = 'classification_edit'),
    path('weplan/classification/classification_remove/<int:pk>/', views.classification_remove, name = 'classification_remove'),
    path('weplan/category', views.category, name = 'category'),
    path('weplan/category/category_new', views.category_new, name = 'category_new'),
    path('weplan/category/category_edit/<int:pk>/', views.category_edit, name = 'category_edit'),
    path('weplan/category/category_remove/<int:pk>/', views.category_remove, name = 'category_remove'),
 #   path('weplan/cai/classification', views.cai_classification, name='cai_classification'),
 #   path('weplan/cai/new_classification', views.new_cai_classification, name='new_cai_classification'),
    path('weplan/classification/crud', views.crud, name='crud'),
    path('affiliate', views.affiliate, name='affiliate'),
    path('home', views.home, name='home'),
    path('home/webfiction', views.webfiction, name='webfiction'),
    path('home/uncapitalizedstartup', views.uncapitalizedstartup, name='uncapitalizedstartup'),
    path('home/digitalnomad', views.digitalnomad, name='digitalnomad'),

]