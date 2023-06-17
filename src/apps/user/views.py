from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.user.models import User
from apps.user.serializers import RegisterUserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    """ User registration """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer
