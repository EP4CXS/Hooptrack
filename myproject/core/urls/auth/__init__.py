"""
Authentication URL patterns for HTML views.

Aggregates login, register, and logout endpoints.
"""

from django.urls import path
from core.views.auth import login, register, logout

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='login'),
    path('register/', register.RegisterView.as_view(), name='register'),
    path('logout/', logout.LogoutView.as_view(), name='logout'),
]
