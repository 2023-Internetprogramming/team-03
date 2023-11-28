from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    departure_location = models.CharField(max_length=50)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    available_seats = models.IntegerField()
    description = models.TextField()

    join_list = models.ManyToManyField(
        User,
        blank=True,
        related_name='ride_user'
    )
    
    def __str__(self):
        return f"{self.departure_location} -> {self.destination}"
