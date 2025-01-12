from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, User


class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        action = request.query_params.get('act')

        if action == 'signup':
            return self.signup(request)
        elif action == 'signin':
            return self.signin(request)
        else:
            return Response({'error': 'Invalid action specified. Use "signup" or "signin".'},
                            status=status.HTTP_400_BAD_REQUEST)

    def signup(self, request):
        """Create a new user account"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'User created successfully.'}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def signin(self, request):
        """Authenticate user and return token"""
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Incorrect password.'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_202_ACCEPTED)


user_api_view = UserAPIView.as_view()
