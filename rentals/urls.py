from django.urls import path

from rentals.views import rental_api_view

urlpatterns = [
    path('rental_api_view/', rental_api_view, name='rental_api_view'),
]
