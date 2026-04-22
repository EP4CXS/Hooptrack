"""
User registration service.

Handles creation of new user accounts with proper validation
and any associated actions (welcome emails, default profiles, etc.).
"""

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class RegisterService:
    """
    Service for user registration.

    Encapsulates all business logic for creating new user accounts,
    including validation, hashing, and post-creation setup.
    """

    @staticmethod
    def execute(email, password, username=None, **extra_fields):
        """
        Register a new user.

        Args:
            email: User's email address (required)
            password: User's password (required)
            username: Optional username (defaults to email)
            **extra_fields: Additional user fields

        Returns:
            User: The created user object

        Raises:
            ValidationError: If user already exists or validation fails
        """
        # TODO: Implement user creation
        # if username is None:
        #     username = email
        # if User.objects.filter(email=email).exists():
        #     raise ValidationError("User with this email already exists")
        #
        # user = User.objects.create(
        #     email=email,
        #     username=username,
        #     password=make_password(password),
        #     **extra_fields
        # )
        # TODO: Send welcome email, create profile, etc.
        # return user
        raise ValidationError("Not implemented")
