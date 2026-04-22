"""
User profile API endpoint.

Allows users to view and update their profile via API.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

class UserProfileAPIView(APIView):
    """
    API endpoint for user profile.

    GET:  Retrieve current user's profile
    PUT:  Update profile information
    PATCH: Partial profile update
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Get current user's profile."""
        user = request.user
        # TODO: Implement profile serialization
        data = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response(data)

    def put(self, request):
        """Update profile."""
        # TODO: Implement profile update
        # serializer = UserProfileSerializer(user, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=400)
        return Response({'status': 'updated'}, status=status.HTTP_200_OK)

    def patch(self, request):
        """Partial profile update."""
        return self.put(request)
