"""
User role and permission models.

Defines roles and permissions specific to user domain.
Can extend Django's built-in permission system.
"""

from django.db import models

# class UserRole(models.Model):
#     """Role assignment for users."""
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True)
#     users = models.ManyToManyField(
#         'core.User',
#         related_name='roles',
#         blank=True
#     )
#     permissions = models.ManyToManyField(
#         'auth.Permission',
#         blank=True,
#         related_name='user_roles'
#     )
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "User Role"
#         verbose_name_plural = "User Roles"

# Placeholder for future implementation
class UserRole(models.Model):
    """Placeholder UserRole model."""
    pass
