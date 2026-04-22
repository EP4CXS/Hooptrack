"""
Login request validator.

Validates login form data before passing to service layer.
Uses Django Forms or Pydantic for validation.
"""

from django import forms

class LoginRequest(forms.Form):
    """
    Form for validating login requests.

    Validates username/email and password combination.
    """
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Username or Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    def clean(self):
        """Additional validation if needed."""
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            # Additional validation can be added here
            pass

        return cleaned_data
