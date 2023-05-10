from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView



from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/orgName.html')


def inn(request):
    return render(request, 'main/inn.html')


def corner(request):
    return render(request, 'main/corner.html')


def reviews(request):
    return render(request, 'main/reviews.html')


def other(request):
    return render(request, 'main/other.html')


def mainpage(request):
    return render(request, 'main/mainpage.html')


def auth(request):
    return render(request, 'main/register.html')


def reg(request):
    return render(request, 'main/reg.html')