from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ['title']
