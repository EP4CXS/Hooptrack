"""
Authentication permission classes.

Custom permissions specific to authentication endpoints.
"""

from rest_framework import permissions

class IsAuthenticated(permissions.IsAuthenticated):
    """Alias for DRF's built-in authenticated permission."""
    pass

class AllowAny(permissions.AllowAny):
    """Alias for DRF's AllowAny."""
    pass
