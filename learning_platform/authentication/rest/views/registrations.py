"""Views for registration endpoints."""

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from authentication.rest.serializers.registrations import RegistrationSerializer


class RegistrationView(CreateAPIView):
    """View for registration of a new user."""

    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

