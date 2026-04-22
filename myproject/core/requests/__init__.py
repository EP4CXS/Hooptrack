"""
Requests package for the Core application.

Request validation layer containing DTOs (Data Transfer Objects),
forms, and validation logic for incoming requests.
This layer sits between views/services and ensures data validity.

Organized by domain:
- auth/:   Authentication request validators
- admin/:  Administrative request validators
- user/:   User-related request validators

Usage pattern:
    from core.requests.auth.login_request import LoginRequest
    login_data = LoginRequest(**request.POST)
    if login_data.is_valid():
        LoginService.execute(login_data)
"""

# Import request validators for convenient access
# from core.requests.auth.login_request import LoginRequest
