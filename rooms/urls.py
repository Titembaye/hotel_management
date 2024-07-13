from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomListView.as_view(), name='rooms-home'),
    path('reserve/', views.ReservationCreateView.as_view(), name='reserve-room'),
]
