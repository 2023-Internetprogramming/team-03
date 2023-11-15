from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Ride(models.Model):
    departure_location = models.CharField(max_length=50)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    available_seats = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.departure_location} -> {self.destination}"
