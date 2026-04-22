"""
Registration request validator.

Validates new user registration data.
"""

from django import forms
from django.core.exceptions import ValidationError

class RegisterRequest(forms.Form):
    """
    Form for validating user registration.
    """
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    def clean(self):
        """Validate that passwords match and email is unique."""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        email = cleaned_data.get('email')

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords do not match")

        # Check email uniqueness (to be implemented when User model is available)
        # from django.contrib.auth import get_user_model
        # User = get_user_model()
        # if User.objects.filter(email=email).exists():
        #     raise ValidationError("Email already registered")

        return cleaned_data
