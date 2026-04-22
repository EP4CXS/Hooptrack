"""
Custom permission classes for the API.

Organized by domain:
- auth/:   Authentication/authorization permissions
- admin/:  Admin-only permissions
- user/:   User-specific permissions

Usage:
    from core.api.permissions.admin import IsAdminOrReadOnly
    permission_classes = [IsAdminOrReadOnly]
"""

# Import permissions for convenience
# from core.api.permissions.admin import IsAdminUser
# from core.api.permissions.user import IsOwnerOrReadOnly
