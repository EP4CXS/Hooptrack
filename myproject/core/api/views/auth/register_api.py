"""
User registration API endpoint.

Handles new user creation via REST API.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

class RegisterAPIView(APIView):
    """
    API endpoint for user registration.

    Creates new user accounts and returns user data.
    POST /api/auth/register/
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Register a new user.

        Expected data:
            {
                "email": "user@example.com",
                "username": "user123",
                "password": "securepassword123",
                "password_confirm": "securepassword123"
            }
        """
        # TODO: Implement user registration
        # serializer = RegisterSerializer(data=request.data)
        # if serializer.is_valid():
        #     user = serializer.save()
        #     refresh = RefreshToken.for_user(user)
        #     return Response({
        #         'refresh': str(refresh),
        #         'access': str(refresh.access_token),
        #         'user': RegisterSerializer(user).data
        #     }, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {'detail': 'Not implemented'},
            status=status.HTTP_501_NOT_IMPLEMENTED
        )
