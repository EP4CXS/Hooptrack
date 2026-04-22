"""
Admin dashboard API endpoint.

Provides statistical data and overview for admin users.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

class AdminDashboardAPIView(APIView):
    """
    API endpoint for admin dashboard statistics.

    Returns overview statistics for administrative dashboard.
    GET /api/admin/dashboard/
    """
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """
        Retrieve admin dashboard statistics.

        Returns:
            {
                "total_users": 150,
                "active_users": 120,
                "new_users_today": 5,
                "system_status": "healthy"
            }
        """
        # TODO: Implement statistics gathering
        # stats = AdminService.get_dashboard_stats()
        stats = {
            'total_users': 0,
            'active_users': 0,
            'new_users_today': 0,
            'system_status': 'healthy',
        }
        return Response(stats)
