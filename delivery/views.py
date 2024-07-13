from django.shortcuts import render
from django.http import HttpResponse

def delivery_home(request):
    return HttpResponse("Bienvenue au restaurant")
