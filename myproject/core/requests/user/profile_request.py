"""
User profile request validators.

Specific to user profile data validation and file uploads.
"""

from django import forms

class AvatarUploadRequest(forms.Form):
    """
    Form for uploading user avatar.
    """
    avatar = forms.ImageField()

    def clean_avatar(self):
        """Validate image file."""
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            # Validate file size (max 5MB)
            if avatar.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Image file too large (max 5MB)")
            # Validate file type
            if not avatar.content_type.startswith('image/'):
                raise forms.ValidationError("File must be an image")
        return avatar

class UserPreferencesRequest(forms.Form):
    """
    Form for updating user preferences.
    """
    theme = forms.ChoiceField(
        required=False,
        choices=[
            ('light', 'Light'),
            ('dark', 'Dark'),
            ('auto', 'Auto'),
        ]
    )
    items_per_page = forms.IntegerField(
        required=False,
        min_value=10,
        max_value=100,
        initial=20
    )
    default_view = forms.ChoiceField(
        required=False,
        choices=[
            ('list', 'List'),
            ('grid', 'Grid'),
            ('compact', 'Compact'),
        ]
    )
