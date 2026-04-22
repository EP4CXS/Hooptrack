"""
Logout API URL patterns.
"""

from django.urls import path
from core.api.views.auth import logout_api

urlpatterns = [
    path('logout/', logout_api.LogoutAPIView.as_view(), name='api-logout'),
]
