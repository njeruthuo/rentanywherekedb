from .models import Rental
from rest_framework import  serializers

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rental
        fields = '__all__'
