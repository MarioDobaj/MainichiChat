from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'homepage/homepage.html', context)

def register(request):
    context = {}
    return render(request, 'homepage/register.html', context)

def privacy(request):
    context = {}
    return render(request, 'homepage/homepage.html', context)
