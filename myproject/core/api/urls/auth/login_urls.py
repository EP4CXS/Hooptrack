"""
Login API URL patterns.
"""

from django.urls import path
from core.api.views.auth import login_api

urlpatterns = [
    path('login/', login_api.LoginAPIView.as_view(), name='api-login'),
]
