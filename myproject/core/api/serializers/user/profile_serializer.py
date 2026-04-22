"""
User profile serializer.

Handles user profile data serialization and validation.
"""

from rest_framework import serializers

class UserProfileSerializer(serializers.Serializer):
    """
    Serializer for user profile.
    """
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    bio = serializers.CharField(required=False, allow_blank=True, max_length=500)
    location = serializers.CharField(required=False, allow_blank=True, max_length=100)
    website = serializers.URLField(required=False, allow_blank=True)
    avatar = serializers.ImageField(required=False, allow_null=True)
    preferences = serializers.JSONField(required=False, default=dict)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
