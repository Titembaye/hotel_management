from django.shortcuts import render
from django.http import request,response
from django.utils.translation import gettext as _

def home(request):
    var = _("Welcome text")
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.post["to_lang"]
    return render(request, 'pages/home.html', {'var':var})


def rooms(request):
    var = _("Welcome text")
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.post["to_lang"]
    return render(request, 'pages/rooms.html', {'var':var})


def restaurant(request):
    var = _("Welcome text")
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.post["to_lang"]
    return render(request, 'pages/restaurant.html', {'var':var})


def contact(request):
    var = _("Welcome text")
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.post["to_lang"]
    return render(request, 'pages/contact.html', {'var':var})


def about(request):
    var = _("Welcome text")
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.post["to_lang"]
    return render(request, 'pages/about.html', {'var':var})

"""
from django.shortcuts import render
from django.utils.translation import gettext as _

def home(request):
    context = {
        'welcome_message': _("Welcome to our hotel."),
    }
    return render(request, 'home.html', context)
"""