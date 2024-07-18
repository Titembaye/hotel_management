from django.db import models

from django.db import models
from users.models import CustomUser

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)



class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title if self.title else str(self.image)


