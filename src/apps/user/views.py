from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.user.models import User
from apps.user.serializers import (
    RegisterUserSerializer,
    LoginTelegramUserSerializer,
    UserSerializer
)


class RegisterUserAPIView(generics.CreateAPIView):
    """ User registration """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer


class CheckTelegramUserApiView(generics.RetrieveAPIView):
    lookup_field = 'telegram_id'
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class LoginTelegramUserApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginTelegramUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.telegram_id = data.get('telegram_id')
        user.save()
        return Response(status=status.HTTP_200_OK)
