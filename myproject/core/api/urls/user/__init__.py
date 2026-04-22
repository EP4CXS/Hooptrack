"""
User API URL configuration.

Aggregates all user-related endpoint URLs.
"""

from django.urls import include, path

urlpatterns = [
    path('dashboard/', include('core.api.urls.user.dashboard_urls')),
    path('profile/', include('core.api.urls.user.profile_urls')),
]
