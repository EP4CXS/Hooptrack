"""
Selectors package for the Core application.

Selector pattern implementation for read-only data queries.
Selectors encapsulate query logic and return DTOs or simple data structures.
This separation keeps query logic out of services and views.

Organized by domain:
- admin/:  Selectors for administrative data
- user/:   Selectors for user-related data

Usage pattern:
    from core.selectors.user.user_selector import UserSelector
    user_data = UserSelector.get_user_by_id(user_id)
"""

# Import selectors for convenient access
# from core.selectors.user.user_selector import UserSelector
