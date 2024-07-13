from django.db import models
from restaurant.models import Order

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    delivery_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
