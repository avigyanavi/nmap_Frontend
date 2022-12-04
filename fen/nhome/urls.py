
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Home/', views.home, name='home'),
    path('Help/', views.help, name='help'),
    path('Readme/', views.readme, name='readme'),
    path('Scans/', views.scans, name='scans'),
    path('Hosts/', views.hosts, name='hosts'),
    path('signin/', views.signin, name='signin'),
]