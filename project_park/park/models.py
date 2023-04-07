from django.db import models

# Create your models here.
from django.db import models

class ParkingSlot(models.Model):
    name = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    occupied_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class History(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    parking_slot = models.CharField(max_length=50)
    occupied_time = models.DateTimeField()
    left_time = models.DateTimeField()

    def __str__(self):
        return self.name
