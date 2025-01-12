from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ReviewAPIView(APIView):

    def get(self, request, *args, **kwargs):
        return  Response({}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_202_ACCEPTED)

review_api_view = ReviewAPIView.as_view()