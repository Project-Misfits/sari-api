import django.contrib.auth.password_validation as validators
from django.contrib.auth import authenticate
from django.core import exceptions
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from dj_rest_auth.serializers import UserDetailsSerializer

from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD

    def is_valid_email(self, payload):
        validator = EmailValidator()
        try:
            validator(payload)
            return True
        except ValidationError:
            return False

    def validate(self, attrs):
        self.context.get("request")

        val = attrs.get("email", None)
        is_email = self.is_valid_email(val)

        try:
            if is_email:
                user_instance = User.objects.get(email=val.lower())
            else:
                user_instance = User.objects.get(username=val.lower())
                attrs["email"] = user_instance.email
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")

        user = authenticate(email=user_instance.email, password=attrs["password"])

        if not user_instance.is_active:
            raise serializers.ValidationError("Account is not active, check your inbox for the activation email.")
        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        data = super().validate(attrs)
        return data


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password", "confirm_password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"}
            },
            "confirm_password": {
                "write_only": True,
                "style": {"input_type": "password"}
            },
            "is_active": {
                "read_only": True,
            }
        }

    def create(self, validated_data):
        # Create and return a new user
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"]
        )

        return user

    def validate(self, data):
        user = self.instance

        errors = dict()
        try:
            validators.validate_password(password=data.get("password"), user=user)
        except exceptions.ValidationError as e:
            errors["password"] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError("Password does not match")
        return data


class CustomUserDetailSerializer(UserDetailsSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name",)  # Add or remove fields
