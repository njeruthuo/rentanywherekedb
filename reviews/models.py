from django.db import models
from rentals.models import Rental

class Messages(models.Model):
    rating = models.IntegerField()
    text = models.TextField()
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)

