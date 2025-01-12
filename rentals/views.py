from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RentalSerializer, Rental

class RentalAPIView(APIView):

    def get(self, request, *args, **kwargs):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True).data
        return  Response(serializer, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_202_ACCEPTED)

rental_api_view = RentalAPIView.as_view()
