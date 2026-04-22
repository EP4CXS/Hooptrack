"""
API package for Django REST Framework endpoints.

This package contains all REST API views, serializers, URLs, and permissions.
The API is organized by domain using subfolders:
- views/:      API view classes (APIView, GenericAPIView, ViewSet)
- serializers/: DRF serializers for model/request serialization
- urls/:       URL routing for API endpoints
- permissions/: Custom permission classes

All API endpoints are prefixed with /api/ from the main urls.py.
"""

# Import API components for convenient access
# from core.api.views.auth.login_api import LoginAPIView
