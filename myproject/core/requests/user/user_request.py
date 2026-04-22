"""
User request validators.

Validates user-related input data for registration,
profile updates, and account operations.
"""

from django import forms

class UserProfileUpdateRequest(forms.Form):
    """
    Form for updating user profile.
    """
    email = forms.EmailField(required=False)
    username = forms.CharField(max_length=150, required=False)
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False, max_length=500)
    location = forms.CharField(max_length=100, required=False)
    website = forms.URLField(required=False)

class UserSettingsRequest(forms.Form):
    """
    Form for updating user settings/preferences.
    """
    email_notifications = forms.BooleanField(required=False)
    sms_notifications = forms.BooleanField(required=False)
    language = forms.ChoiceField(
        required=False,
        choices=[
            ('en', 'English'),
            ('es', 'Spanish'),
            ('fr', 'French'),
        ]
    )
    timezone = forms.CharField(max_length=50, required=False)
