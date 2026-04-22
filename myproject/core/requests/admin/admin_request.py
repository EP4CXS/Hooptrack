"""
Administrative request validators.

Contains forms/validators for admin operations like
user management, system configuration, etc.
"""

from django import forms

class AdminUserSearchRequest(forms.Form):
    """
    Form for searching/filtering users in admin panel.
    """
    query = forms.CharField(required=False, max_length=100)
    status = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'All'),
            ('active', 'Active'),
            ('inactive', 'Inactive'),
        ]
    )
    role = forms.CharField(required=False, max_length=50)

class SystemConfigRequest(forms.Form):
    """
    Form for updating system configuration.
    """
    site_name = forms.CharField(max_length=100)
    maintenance_mode = forms.BooleanField(required=False)
    registration_enabled = forms.BooleanField(required=False)
