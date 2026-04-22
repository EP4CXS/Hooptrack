"""
Custom API response utilities.

Standardized response format for API endpoints.
"""

from rest_framework.response import Response
from rest_framework import status

def success_response(data=None, message="Success", code=status.HTTP_200_OK):
    """
    Return a standardized success response.

    Args:
        data: Response data
        message: Success message
        code: HTTP status code

    Returns:
        Response: DRF Response object
    """
    return Response({
        'success': True,
        'message': message,
        'data': data or {},
    }, status=code)

def error_response(message="Error", code=status.HTTP_400_BAD_REQUEST, errors=None):
    """
    Return a standardized error response.

    Args:
        message: Error message
        code: HTTP status code
        errors: Detailed error information

    Returns:
        Response: DRF Response object
    """
    return Response({
        'success': False,
        'message': message,
        'errors': errors or {},
    }, status=code)
