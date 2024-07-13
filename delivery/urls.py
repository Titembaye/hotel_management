from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_home, name='restaurant-home'),
]
