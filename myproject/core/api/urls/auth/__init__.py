"""
Authentication API URL configuration.

Aggregates all authentication-related endpoint URLs.
"""

from django.urls import include, path

urlpatterns = [
    path('login/', include('core.api.urls.auth.login_urls')),
    path('register/', include('core.api.urls.auth.register_urls')),
    path('logout/', include('core.api.urls.auth.logout_urls')),
]
