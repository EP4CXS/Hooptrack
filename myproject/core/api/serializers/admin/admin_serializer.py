"""
Admin serializer for admin user data.

Used for listing and managing admin users.
"""

from rest_framework import serializers

class AdminSerializer(serializers.Serializer):
    """
    Serializer for admin user representation.
    """
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    is_staff = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField()
    date_joined = serializers.DateTimeField(read_only=True)

    # TODO: Convert to ModelSerializer when User model is defined
    # class Meta:
    #     model = User
    #     fields = ['id', 'email', 'username', ...]
