"""
User URL patterns for HTML views.

Aggregates user dashboard and profile endpoints.
"""

from django.urls import path
from core.views.user import dashboard, profile

urlpatterns = [
    path('', dashboard.UserDashboardView.as_view(), name='user-dashboard'),
    path('profile/', profile.UserProfileView.as_view(), name='user-profile'),
]
