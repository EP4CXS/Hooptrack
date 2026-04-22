"""
Admin URL patterns for HTML views.

Aggregates admin dashboard and management endpoints.
"""

from django.urls import path
from core.views.admin import dashboard, management

urlpatterns = [
    path('', dashboard.AdminDashboardView.as_view(), name='admin-dashboard'),
    path('users/', management.UserManagementView.as_view(), name='admin-users'),
    path('config/', management.SystemConfigView.as_view(), name='admin-system-config'),
]
