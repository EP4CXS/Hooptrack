"""
User profile API URL patterns.
"""

from django.urls import path
from core.api.views.user import profile_api

urlpatterns = [
    path('profile/', profile_api.UserProfileAPIView.as_view(), name='api-user-profile'),
]
