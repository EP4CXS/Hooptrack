"""
Logout request validator.

Typically minimal validation needed for logout.
Placeholder for consistency with request pattern.
"""

from django import forms

class LogoutRequest(forms.Form):
    """
    Form for logout (typically no fields needed).
    """
    # Placeholder - logout usually doesn't require form data
    # Could include CSRF token validation
    pass
