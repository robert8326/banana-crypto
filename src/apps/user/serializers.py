from abc import ABC

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from apps.user.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    """ User registration serializer """
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'password2',
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('username'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class LoginTelegramUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    telegram_id = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'telegram_id', 'is_superuser')
