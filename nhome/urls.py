
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('scans/', views.scans, name='scans'),
    path('hosts/', views.hosts, name='hosts'),
    path('signin/', views.signin, name='signin'),
    path('visitorlog/', views.visitorlog, name='visitorlog'),
    path('visitorlog/add/', views.add, name='add'),
    path('visitorlog/add/addrecord/', views.addrecord, name='addrecord'),
]