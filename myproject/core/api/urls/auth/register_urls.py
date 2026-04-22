"""
Register API URL patterns.
"""

from django.urls import path
from core.api.views.auth import register_api

urlpatterns = [
    path('register/', register_api.RegisterAPIView.as_view(), name='api-register'),
]
