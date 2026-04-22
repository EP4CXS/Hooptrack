"""
Admin permission classes.

Permissions for administrative access control.
"""

from rest_framework import permissions

class IsAdminUser(permissions.IsAdminUser):
    """Alias for DRF's built-in admin user permission."""
    pass

class IsSuperUser(permissions.BasePermission):
    """Permission for superuser-only access."""
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Allow read access to all, write access to staff only.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
