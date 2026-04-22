"""
User profile model.

Extends the User model with additional profile information.
Separate from the main User model to keep concerns separated.
"""

from django.db import models

# class UserProfile(models.Model):
#     """Additional profile information for users."""
#     user = models.OneToOneField(
#         'core.User',  # or settings.AUTH_USER_MODEL
#         on_delete=models.CASCADE,
#         related_name='profile'
#     )
#     bio = models.TextField(blank=True, max_length=500)
#     location = models.CharField(max_length=100, blank=True)
#     website = models.URLField(blank=True)
#     avatar = models.ImageField(
#         upload_to='avatars/',
#         null=True,
#         blank=True
#     )
#     preferences = models.JSONField(default=dict, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"Profile for {self.user.email}"
#
#     class Meta:
#         verbose_name = "User Profile"
#         verbose_name_plural = "User Profiles"

# Placeholder for future implementation
class UserProfile(models.Model):
    """Placeholder UserProfile model."""
    pass
