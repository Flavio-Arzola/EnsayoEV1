from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse("<h1>Hola mundo!</h1>")

def display2(request):
    return HttpResponse("<h1>Hola mundo 2!</h1>")

# Create your views here.
