from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomListView.as_view(), name='rooms-home'),
    path('reserve/', views.ReservationCreateView.as_view(), name='reserve-room'),

    path('gallery/', views.gallery_list_view, name='gallery_list'),
    path('gallery/add/', views.gallery_create_view, name='gallery_create'),
    path('gallery/<int:pk>/edit/', views.gallery_update_view, name='gallery_update'),
    path('gallery/<int:pk>/delete/', views.gallery_delete_view, name='gallery_delete'),
]
