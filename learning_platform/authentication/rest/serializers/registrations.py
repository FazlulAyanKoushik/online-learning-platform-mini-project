"""Serializer for registration of a new user"""
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializer for registration of a new user"""
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
            "email",
        ]

    def validate(self, data):
        # Check if the password and confirm_password match

        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError({'confirm_password': "Passwords do not match."})

        return data

    def create(self, validated_data):
        # Remove the confirm_password from the validated data
        validated_data.pop('confirm_password')

        # Extract the username from the validated data
        username = validated_data.get('username')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                {"username": "This username is already taken."}
            )

        # Create a new user
        user = User.objects.create_user(
            **validated_data
        )

        return user
