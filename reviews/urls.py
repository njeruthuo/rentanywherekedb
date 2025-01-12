from django.urls import path
from .views import review_api_view

urlpatterns = [
    path('review_api_view/',review_api_view, name='review_api_view'),
]

