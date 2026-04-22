"""
User model for authentication and user management.

This is the primary User model for the application.
Replace or extend Django's built-in User model as needed.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# Option 1: Extend Django's AbstractUser (recommended)
#
# class User(AbstractUser):
#     """Custom User model extending Django's AbstractUser."""
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20, blank=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     profile_picture = models.ImageField(
#         upload_to='profile_pics/',
#         null=True,
#         blank=True
#     )
#     is_verified = models.BooleanField(default=False)
#     verification_token = models.CharField(max_length=100, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"
#         ordering = ['-created_at']

# Option 2: Use Django's default User model
# If using default, no custom model needed here.
# Simply reference the built-in User in your code:
# from django.contrib.auth.models import User

# Placeholder for future User model implementation
class User(models.Model):
    """
    Placeholder User model.
    Implement with proper fields as needed.
    """
    pass
