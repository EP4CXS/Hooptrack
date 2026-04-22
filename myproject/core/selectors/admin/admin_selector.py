"""
Admin domain selectors.

Read-only query operations for administrative data.
These selectors fetch data without modifying state.
"""

class AdminSelector:
    """
    Selector for admin-related queries.
    """

    @staticmethod
    def get_active_admins():
        """
        Get all active admin users.

        Returns:
            QuerySet: Active admin users
        """
        # TODO: Implement query
        # from django.contrib.auth import get_user_model
        # User = get_user_model()
        # return User.objects.filter(is_staff=True, is_active=True)
        return None

    @staticmethod
    def get_superusers():
        """
        Get all superuser accounts.

        Returns:
            QuerySet: Superuser objects
        """
        # TODO: Implement query
        # from django.contrib.auth import get_user_model
        # User = get_user_model()
        # return User.objects.filter(is_superuser=True)
        return None
