# MyProject in Programming Languages

A scalable, professional Django project scaffold implementing a clean layered architecture with domain separation.

## Overview

This project provides a structured foundation for building Django applications with this:
- Authentication system
- Admin domain
- User domain
- API-first design with DRF
- Request validation pattern
- Service layer pattern
- Selector pattern for data retrieval
- Domain-driven folder separation

The architecture follows a layered approach where each major layer (models, views, services, requests, selectors, forms, tests, api) is organized by domain using subfolders rather than monolithic files.

## Architecture

```
myproject/
├── config/             
│   ├── settings/       
│   │   ├── base.py     
│   │   ├── local.py    
│   │   └── production.py 
│   ├── urls.py          
│   └── asgi.py/wsgi.py 
│
├── core/              
│   ├── models/         # Domain-separated models
│   │   ├── admin/      # Admin domain models
│   │   └── user/       # User domain models
│   ├── views/          # Domain-separated views
│   │   ├── auth/
│   │   ├── admin/
│   │   └── user/
│   ├── services/       # Business logic layer
│   ├── requests/       # Request validation layer (DTOs/forms)
│   ├── selectors/      # Data retrieval layer (queries)
│   ├── api/            # REST API (views, serializers, urls, permissions)
│   ├── urls/           # App-level URL configs
│   ├── middleware/     # Custom middleware
│   ├── utils/          # Utility functions
│   ├── forms/          # Django forms
│   └── tests/          # Domain-separated tests
│
├── templates/          # HTML templates
├── static/             # Static assets (CSS, JS, images)
├── media/              # User-uploaded files
└── manage.py           # Django CLI utility
```

## Key Design Principles

1. **Domain Separation**: Each major layer uses subfolders for domains (admin, user, auth) rather than single monolithic files
2. **Split Settings**: Configuration split by environment (base/local/production)
3. **Service Layer**: Business logic isolated from UI
4. **Request Validation**: Dedicated request objects for input validation
5. **Selector Pattern**: Query logic separated from business logic
6. **API First**: Clear separation between web views and API endpoints
7. **Test Organization**: Tests organized by domain and type

## Setup Instructions

### 1. Clone OR Download Project

Place the `myproject` folder in your development environment.

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your actual values (database credentials, secret key, etc.)
```

### 5. Database Setup

```bash
# Create PostgreSQL database (if using PostgreSQL)
# Or SQLite will work with default settings

# Apply migrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit:
- Admin interface: http://127.0.0.1:8000/admin/
- API root: http://127.0.0.1:8000/api/

## Project Structure Summary

- **config/**: Django project configuration with split settings
- **core/**: Main application containing all business domains
  - **models/**: Database models separated by domain
  - **views/**: HTTP request handlers (HTML responses)
  - **services/**: Business logic implementation
  - **requests/**: Input validation and DTOs
  - **selectors/**: Read query objects
  - **api/**: REST API endpoints with DRF
  - **urls/**: URL routing patterns
  - **forms/**: Django form definitions
  - **tests/**: Automated tests
  - **middleware/**: Custom middleware components
  - **utils/**: Helper functions and utilities
- **templates/**: HTML templates directory
- **static/**: Static files (CSS, JS, images)
- **media/**: User uploads directory

## Important Notes

This is a **scaffold-only** project. It contains the complete folder architecture and minimal valid boilerplate code, but NO business-specific implementation yet.

All domain files (models, views, services, etc.) are empty placeholders ready for feature development. The project is configured with common Django dependencies (DRF, JWT, CORS, filtering) and is ready for:
- User authentication implementation
- Admin functionality
- User management features
- API endpoint development
- Custom business logic

## Next Steps

1. Implement User model in `core/models/user/user.py`
2. Create authentication services in `core/services/auth/`
3. Build API endpoints in `core/api/views/`
4. Add domain-specific models in respective `models/` subfolders
5. Implement selectors for read operations
6. Create request validators for input handling
7. Write domain-specific tests

## Dependencies

- Django 5.x
- Django REST Framework 3.15+
- SimpleJWT for JWT authentication
- PostgreSQL support (psycopg2-binary)
- CORS headers for cross-origin requests
- Django Filter for filtering
- DRF Yasg for API documentation
- Pillow for image handling
- python-decouple for environment variables

## License

This project scaffold is provided as-is for educational and commercial use.
