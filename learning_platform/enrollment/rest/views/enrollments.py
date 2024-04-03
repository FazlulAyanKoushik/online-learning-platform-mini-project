"""Views for the enrollment model."""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from enrollment.models import Enrollment
from enrollment.rest.serializers.enrollments import (
    EnrollmentSerializer,
    EnrollmentDetailSerializer,
)


class EnrollmentListCreateAPIView(ListCreateAPIView):
    """View for listing and creating enrollments"""
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        return Enrollment.objects.all()


class EnrollmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting enrollments"""
    serializer_class = EnrollmentSerializer
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return EnrollmentDetailSerializer
        return EnrollmentSerializer

    def get_queryset(self):
        return Enrollment.objects.all()
