"""
Login serializer for API authentication.

Validates login credentials and returns tokens.
"""

from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    """
    Serializer for login request validation.

    Validates username/email and password.
    """
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """Validate credentials."""
        # TODO: Implement authentication validation
        # from django.contrib.auth import authenticate
        # user = authenticate(
        #     username=data.get('username'),
        #     password=data.get('password')
        # )
        # if user is None:
        #     raise serializers.ValidationError("Invalid credentials")
        # data['user'] = user
        return data
