"""
Django app configuration for the Core app.

This app serves as the main application container for all business domains:
- Authentication
- Admin
- User management
- Business logic layers (services, selectors, requests)
- REST API
- Forms and validation
- Utils and middleware
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Application configuration for the Core app.

    Provides a central container for all domain-specific modules.
    The Core app is the primary application containing authentication,
    admin, and user domains with their respective models, views,
    services, and API endpoints.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        """
        Perform initialization when the app is ready.

        Import signals to ensure they are registered.
        """
        import core.signals  # noqa
