from django.shortcuts import render
from django.http import HttpResponse

def restaurant_home(request):
    return HttpResponse("Bienvenue au restaurant")
