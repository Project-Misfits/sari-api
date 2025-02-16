import django.contrib.auth.password_validation as validators
from django.contrib.auth import authenticate
from django.core import exceptions

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from dj_rest_auth.serializers import UserDetailsSerializer

from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD

    def validate(self, attrs):
        self.context.get('request')
        password = None
        try:
            user_instance = User.objects.get(email=attrs["email"].lower())
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")

        user = authenticate(email=attrs['email'].lower(), password=password)
        if not user_instance.is_active:
            raise serializers.ValidationError("Account is not active, check your inbox for the activation email.")
        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        attrs["password"] = password
        data = super().validate(attrs)
        return data


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'confirm_password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'is_active': {
                'read_only': True,
            }
        }

    def create(self, validated_data):
        # Create and return a new user
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        return user

    def validate(self, data):
        user = self.instance

        errors = dict()
        try:
            validators.validate_password(password=data.get('password'), user=user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Password does not match")
        return data


class CustomUserDetailSerializer(UserDetailsSerializer):

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name",)  # Add or remove fields
