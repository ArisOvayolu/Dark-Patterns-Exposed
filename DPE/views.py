from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'index.html')

def dpt(request):
    return render(request, 'DarkPatternTechniques.html')

def contact(request):
    return render(request, 'contact.html')

def etdp(request):
    return render(request, 'ExposeTheDarkPatterns.html')

# Create your views here.
