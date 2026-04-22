"""
Admin management API URL patterns.
"""

from django.urls import path
from core.api.views.admin import management_api

urlpatterns = [
    path('users/', management_api.UserManagementListAPIView.as_view(), name='api-admin-users'),
    path('users/<int:user_id>/', management_api.UserManagementDetailAPIView.as_view(), name='api-admin-user-detail'),
]
