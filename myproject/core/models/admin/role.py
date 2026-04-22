"""
Admin role and permission models.

This module contains models for administrative roles, permissions,
and access control. Currently a placeholder for future implementation.
"""

from django.db import models

# Create your admin role/permission models here.
#
# Example:
#
# class AdminRole(models.Model):
#     """Defines roles for administrative users."""
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True)
#     permissions = models.ManyToManyField(
#         'auth.Permission',
#         blank=True,
#         related_name='admin_roles'
#     )
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
# class AdminPermission(models.Model):
#     """Custom permissions for admin domain."""
#     code = models.CharField(max_length=100, unique=True)
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     resource = models.CharField(max_length=100)  # e.g., 'user', 'order', 'report'
#
#     def __str__(self):
#         return f"{self.resource}:{self.code}"
