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
    path('affiliate', views.affiliate, name='affiliate'),
    path('home', views.home, name='home'),
    path('home/webfiction', views.webfiction, name='webfiction'),
    path('home/uncapitalizedstartup', views.uncapitalizedstartup, name='uncapitalizedstartup'),
    path('home/digitalnomad', views.digitalnomad, name='digitalnomad'),
]
