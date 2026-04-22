"""
User permission classes.

Permissions for user-specific access control.
"""

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners to edit.
    Assumes the model instance has a `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only to owner
        return obj.user == request.user

class IsSelf(permissions.BasePermission):
    """
    Permission to only allow users to access their own data.
    """
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
