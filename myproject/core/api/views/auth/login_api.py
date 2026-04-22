"""
Login API endpoint.

Handles authentication via REST API.
Returns JWT tokens upon successful authentication.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPIView(APIView):
    """
    API endpoint for user login.

    Accepts credentials and returns JWT access and refresh tokens.
    POST /api/auth/login/
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Authenticate user and return JWT tokens.

        Expected data:
            {
                "username": "user@example.com",
                "password": "password123"
            }
        """
        # TODO: Implement authentication
        # username = request.data.get('username')
        # password = request.data.get('password')
        # user = authenticate(username=username, password=password)
        #
        # if user is None:
        #     return Response(
        #         {'error': 'Invalid credentials'},
        #         status=status.HTTP_401_UNAUTHORIZED
        #     )
        #
        # refresh = RefreshToken.for_user(user)
        # return Response({
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token),
        #     'user': {
        #         'id': user.id,
        #         'email': user.email,
        #         'username': user.username,
        #     }
        # })

        return Response(
            {'detail': 'Not implemented'},
            status=status.HTTP_501_NOT_IMPLEMENTED
        )
