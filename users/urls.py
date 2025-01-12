from .views import user_api_view
from django.urls import path

urlpatterns = [
    path('user_api_view/', user_api_view, name='user_api_view'),
]