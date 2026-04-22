"""
URL routing for the Core application (HTML views).

This module aggregates URL patterns from domain-specific modules.
All URLs defined here are included under the root URLconf (config.urls).

Structure:
    '' (root)          - Home page / landing
    auth/              - Authentication views (login, register, logout)
    admin/             - Admin dashboard and management
    user/              - User dashboard and profile

Each domain's URLs are defined in their respective submodule.
"""

from django.urls import include, path

urlpatterns = [
    # Auth URLs (login, register, logout)
    path('auth/', include('core.urls.auth')),

    # Admin URLs (dashboard, management)
    path('admin/', include('core.urls.admin')),

    # User URLs (dashboard, profile)
    path('user/', include('core.urls.user')),

    # Placeholder for root/home URL
    # path('', core.views.home.HomeView.as_view(), name='home'),
]
