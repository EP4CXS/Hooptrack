"""
Admin profile request validators.

Validates data for admin profile updates and permissions.
"""

from django import forms

class AdminProfileUpdateRequest(forms.Form):
    """
    Form for updating admin profile information.
    """
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    department = forms.CharField(max_length=100, required=False)
    employee_id = forms.CharField(max_length=50, required=False)

class AdminPermissionRequest(forms.Form):
    """
    Form for assigning/modifying admin permissions.
    """
    user_id = forms.IntegerField()
    permissions = forms.CharField(required=False)  # Comma-separated permission IDs

    def clean_permissions(self):
        """Parse permission IDs."""
        permissions = self.cleaned_data.get('permissions', '')
        if permissions:
            return [int(p.strip()) for p in permissions.split(',') if p.strip()]
        return []
