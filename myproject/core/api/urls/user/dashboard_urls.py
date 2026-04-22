"""
User dashboard API URL patterns.
"""

from django.urls import path
from core.api.views.user import dashboard_api

urlpatterns = [
    path('dashboard/', dashboard_api.UserDashboardAPIView.as_view(), name='api-user-dashboard'),
]
