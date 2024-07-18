from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from .models import Room, Reservation, GalleryImage
from .forms import ReservationForm, GalleryImageForm
import os


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






# Create and Read (List)
def gallery_list_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'backend/gallery/gallery_list.html', {'images': images})

# Create
def gallery_create_view(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = GalleryImageForm()
    return render(request, 'backend/gallery/gallery_create.html', {'form': form})

# Update
"""
def gallery_update_view(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = GalleryImageForm(instance=image)
    return render(request, 'gallery/gallery_edit.html', {'form': form})"""


def gallery_update_view(request, pk):
    image = get_object_or_404(GalleryImage, id=pk)
    old_image_path = image.image.path

    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            if request.FILES.get('image'):
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
            form.save()
            return redirect('gallery_list')
    else:
        form = GalleryImageForm(instance=image)

    return render(request, 'backend/gallery/gallery_edit.html', {'form': form, 'image': image})


# Delete
def gallery_delete_view(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery_list')
    return render(request, 'gallery/gallery_confirm_delete.html', {'image': image})



