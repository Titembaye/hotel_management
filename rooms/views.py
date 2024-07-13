from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Room, Reservation
from .forms import ReservationForm

class RoomListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        return Room.objects.filter(is_available=True)

class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'rooms/reservation_form.html'
    success_url = '/rooms/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
