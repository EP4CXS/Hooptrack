"""
Root API URL routing.

Includes all domain-specific API endpoints with prefix /api/.
"""

from django.urls import include, path

urlpatterns = [
    path('auth/', include('core.api.urls.auth')),
    path('admin/', include('core.api.urls.admin')),
    path('user/', include('core.api.urls.user')),
]
