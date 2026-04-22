"""
Administrative forms.

Placeholder for admin-related Django forms.
"""

from django import forms

class UserSearchForm(forms.Form):
    """
    Form for searching users in admin interface.
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

class SystemConfigForm(forms.Form):
    """
    Form for updating system configuration.
    """
    site_name = forms.CharField(max_length=100)
    maintenance_mode = forms.BooleanField(required=False)
    registration_enabled = forms.BooleanField(required=False)
