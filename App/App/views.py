from django.shortcuts import render , redirect
from django.http import HttpResponse


def Home(request):
    context = {}
    return render(request, "Homepage.html")


def LOGIN(request):

    context = {}
    return render(request, "login.html")


def REGISTRATION(request):
    context = {}
    return render(request, "registration.html")