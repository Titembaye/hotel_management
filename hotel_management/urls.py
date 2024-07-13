from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from . import views  # Importez vos vues ici
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('rooms/', views.rooms, name="rooms"),
    path('restaurant/', views.restaurant, name="restaurant"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('users-home/', include('users.urls')),
    path('rooms-home/', include('rooms.urls')),
    path('restaurant-home/', include('restaurant.urls')),
    path('delivery-home/', include('delivery.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
