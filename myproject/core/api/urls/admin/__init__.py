"""
Admin API URL configuration.

Aggregates all administrative endpoint URLs.
"""

from django.urls import include, path

urlpatterns = [
    path('dashboard/', include('core.api.urls.admin.dashboard_urls')),
    path('users/', include('core.api.urls.admin.management_urls')),
]
