# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from fen import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.urls import reverse
from .models import nhome

def index(request):
    return render(request, "nhome/index.html")

def signin(request):
    context = {}
    if request.method == 'POST':
        return render(request, "nhome/Home.html", context)
    return render(request, "nhome/signin.html", context)


def home(request):
    context = {}
    return render(request, 'nhome/home.html', context)
# from django.template import loader
# from django.http import HttpResponse

# def home(request):
#     template = loader.get_template('nhome/Home.html')
#     context = {}
#     return HttpResponse(template.render(context, request))

def help(request):
    context = {}
    return render(request, 'nhome/help.html', context)

def scans(request):
    context = {}
    return render(request, 'nhome/scans.html', context)

def aboutme(request):
    context = {}
    return render(request, 'nhome/aboutme.html', context)

def hosts(request):
    context = {}
    return render(request, 'nhome/hosts.html', context)

def visitorlog(request):
    mymembers = nhome.objects.all().values()
    template = loader.get_template('nhome/visitorlog.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('nhome/add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
    global nhome
    x = request.POST['username']
    y = request.POST['Pass1']
    nhome = nhome(username=x, pass1=y)
    nhome.save()
    return HttpResponseRedirect(reverse('home'))