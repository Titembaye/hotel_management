from django.shortcuts import render
from django.http import request,response
from django.utils.translation import gettext as _

from rooms.models import GalleryImage


def home(request):
    var = _("Welcome text")
    images = GalleryImage.objects.filter(is_visible=True)
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.POST.get('to_lang')
        # Ajoutez votre logique de traitement ici si nécessaire
    return render(request, 'frontend/pages/home.html', {'var': var, 'images': images})


def rooms(request):
    var = _("Welcome text")
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.post["to_lang"]
    return render(request, 'frontend/pages/rooms.html', {'var':var})


def restaurant(request):
    var = _("Welcome text")
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.post["to_lang"]
    return render(request, 'frontend/pages/restaurant.html', {'var':var})


def contact(request):
    var = _("Welcome text")
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.post["to_lang"]
    return render(request, 'frontend/pages/contact.html', {'var':var})


def about(request):
    var = _("Welcome text")
    images = GalleryImage.objects.filter(is_visible=True)
    if request.method == "POST":
        from_lang = request.POST.get('from_lang')
        to_lang = request.post["to_lang"]
    return render(request, 'frontend/pages/about.html', {'var':var, 'images':images})





def gallery_view(request):
    images = GalleryImage.objects.filter(is_visible=True)
    return render(request, 'gallery.html', {'images': images})
"""
from django.shortcuts import render
from django.utils.translation import gettext as _

def home(request):
    context = {
        'welcome_message': _("Welcome to our hotel."),
    }
    return render(request, 'home.html', context)
"""