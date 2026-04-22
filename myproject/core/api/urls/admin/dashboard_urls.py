"""
Admin dashboard API URL patterns.
"""

from django.urls import path
from core.api.views.admin import dashboard_api

urlpatterns = [
    path('dashboard/', dashboard_api.AdminDashboardAPIView.as_view(), name='api-admin-dashboard'),
]
