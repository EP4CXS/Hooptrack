from django.contrib.auth.models import User
from rest_framework import permissions, serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.api.serializers.auth_serializers import RegisterSerializer, UserSerializer

# Mock Philippine-style locations (ids stable for the V2-style cascading selects)
LOCATIONS = {
    "regions": [
        {"id": 1, "name": "Luzon"},
        {"id": 2, "name": "Visayas"},
        {"id": 3, "name": "Mindanao"},
    ],
    "provinces": {
        1: [
            {"id": 11, "name": "Metro Manila"},
            {"id": 12, "name": "Cavite"},
            {"id": 13, "name": "Bulacan"},
        ],
        2: [
            {"id": 21, "name": "Cebu"},
            {"id": 22, "name": "Bohol"},
        ],
        3: [
            {"id": 31, "name": "Davao del Sur"},
            {"id": 32, "name": "Misamis Oriental"},
        ],
    },
    "cities": {
        11: [
            {"id": 111, "name": "Manila"},
            {"id": 112, "name": "Quezon City"},
        ],
        12: [
            {"id": 121, "name": "Bacoor"},
            {"id": 122, "name": "Dasmariñas"},
        ],
        13: [
            {"id": 131, "name": "Malolos"},
            {"id": 132, "name": "San Jose del Monte"},
        ],
        21: [
            {"id": 211, "name": "Cebu City"},
            {"id": 212, "name": "Mandaue"},
        ],
        22: [
            {"id": 221, "name": "Tagbilaran"},
        ],
        31: [
            {"id": 311, "name": "Davao City"},
        ],
        32: [
            {"id": 321, "name": "Cagayan de Oro"},
        ],
    },
}


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("username", None)
        self.fields["email"] = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get("email")
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist as exc:
            raise ValidationError({"detail": "No active account found with the given credentials"}) from exc
        if not user.is_active:
            raise ValidationError({"detail": "No active account found with the given credentials"})
        attrs["username"] = user.get_username()
        attrs.pop("email", None)
        return super().validate(attrs)


class EmailLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EmailTokenObtainPairSerializer


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def locations_regions_view(_request):
    return Response(LOCATIONS["regions"])


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def locations_provinces_view(_request, region_id):
    rows = LOCATIONS["provinces"].get(int(region_id), [])
    return Response(rows)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def locations_cities_view(_request, province_id):
    rows = LOCATIONS["cities"].get(int(province_id), [])
    return Response(rows)


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class RefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "success": True,
                "message": "Registration successful",
                "data": {
                    "user": UserSerializer(user).data,
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                },
            },
            status=status.HTTP_201_CREATED,
        )


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
    refresh_token = request.data.get("refresh")
    if not refresh_token:
        return Response({"success": False, "message": "refresh token is required"}, status=400)
    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response({"success": True, "message": "Logged out"}, status=200)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def me_view(request):
    return Response({"success": True, "data": UserSerializer(request.user).data}, status=200)
