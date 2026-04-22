"""
Logout serializer for token blacklisting.

Validates refresh token for blacklisting.
"""

from rest_framework import serializers

class LogoutSerializer(serializers.Serializer):
    """
    Serializer for logout request.
    """
    refresh = serializers.CharField()

    def validate_refresh(self, value):
        """Validate refresh token."""
        # TODO: Validate token is not already blacklisted
        return value
