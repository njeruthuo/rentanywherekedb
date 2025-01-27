from django.db import models
from users.models import User


class RentalTypeChoices(models.TextChoices):
    SINGLE = 'SINGLE ROOM', 'SR'
    BEDSITTER = 'BEDSITTER', 'BS'
    BR1 = 'ONE BEDROOM', 'BR1'
    BR2 = 'TWO BEDROOM', 'BR2'
    BR3 = 'THREE BEDROOM', 'BR3'
    BR4 = 'FOUR BEDROOM', 'BR4'
    OFFICE = 'OFFICE SPACE', 'OFFICE'
    STALL = 'BUSINESS STALL', 'STALL'


class Rental(models.Model):
    building_name = models.CharField(max_length=200, blank=True)
    room_size = models.JSONField()  # dimensions of the rooms
    location = models.JSONField()  # coordinates to be added from Google Maps.
    rental_type = models.CharField(
        max_length=20, choices=RentalTypeChoices.choices, default=RentalTypeChoices.BEDSITTER)
    distance_from_tarmac = models.CharField(max_length=100)
    distance_from_cbd = models.CharField(max_length=200)
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_required = models.BooleanField(default=True)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vacant = models.BooleanField(default=True)
    area = models.CharField(max_length=250)
    bathrooms = models.IntegerField()
    amenities = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    multi_storey = models.BooleanField(default=False)
    description = models.TextField()  # add info about the rental house.
    date_created = models.DateTimeField(auto_now_add=True)


class RentalImage(models.Model):
    rental = models.ForeignKey(
        Rental, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='rental_images/')
    # Optional caption for the image
    caption = models.CharField(max_length=255, blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
