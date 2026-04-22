"""
Authentication-related permissions.

Custom permissions for auth domain endpoints.
"""

# from rest_framework import permissions
#
# class IsAuthenticated(permissions.IsAuthenticated):
#     """Alias for DRF's built-in IsAuthenticated."""
#     pass
#
# class IsAdminOrReadOnly(permissions.BasePermission):
#     """Allow read access to all, write only to admins."""
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user and request.user.is_staff
