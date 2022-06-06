from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    CustomTokenObtainPairSerializer,
    RegistrationSerializer
)
from drf_yasg.utils import swagger_auto_schema


class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom token pair  API view """
    serializer_class = CustomTokenObtainPairSerializer


class RegistrationView(APIView):
    """ User registration API view definition"""
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            refresh = RefreshToken.for_user(account)
            data['response'] = "Registration Successful !!"
            data['username'] = account.username
            data['email'] = account.email
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
