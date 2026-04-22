"""
Registration serializer for new user creation.

Handles validation and creation of new accounts.
"""

from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    """
    Serializer for user registration.
    """
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    def validate(self, data):
        """Validate passwords match."""
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        """Create new user."""
        # Remove password_confirm from validated data
        validated_data.pop('password_confirm')
        # TODO: Implement user creation
        # from core.services.auth.register_service import RegisterService
        # return RegisterService.execute(**validated_data)
        return None
