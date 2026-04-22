"""
URL configuration for MyProject project.

Includes routes for:
- Django admin site
- Core application URLs (to be implemented)
- API endpoints under /api/
- Media serving in DEBUG mode
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin site
    path('admin/', admin.site.urls),

    # Core application URLs (placeholder)
    # Will be organized by domain in core/urls/
    path('', include('core.urls')),

    # API endpoints under /api/
    path('api/', include('core.api.urls')),
]

# Serve media files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
