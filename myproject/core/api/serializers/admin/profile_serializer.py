"""
Admin profile serializer.

Serializes admin profile data for API responses.
"""

from rest_framework import serializers

class AdminProfileSerializer(serializers.Serializer):
    """
    Serializer for admin profile.
    """
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    department = serializers.CharField(max_length=100)
    employee_id = serializers.CharField(max_length=50)
    supervisor = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    access_level = serializers.IntegerField(min_value=1, default=1)
    created_at = serializers.DateTimeField(read_only=True)
