"""
User dashboard API endpoint.

Returns personalized user dashboard data.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

class UserDashboardAPIView(APIView):
    """
    API endpoint for user dashboard.

    Returns user-specific dashboard information.
    GET /api/user/dashboard/
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Retrieve user dashboard data.

        Returns personalized statistics and recent activity.
        """
        user = request.user
        # TODO: Implement dashboard data retrieval
        data = {
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
            },
            'statistics': {
                'account_age_days': 0,
                'last_login': user.last_login,
            },
            'recent_activity': [],
            'notifications': [],
        }
        return Response(data)
