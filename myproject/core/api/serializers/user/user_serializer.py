"""
User serializer for API responses.

Basic user data representation for API responses.
"""

from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    """
    Serializer for user data.
    """
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    is_active = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
