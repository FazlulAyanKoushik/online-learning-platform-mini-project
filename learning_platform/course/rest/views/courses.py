"""Views for the course model."""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from course.models import Course
from course.rest.serializers.courses import CourseSerializer
from course.filters import CourseFilter


class CourseListCreateAPIView(ListCreateAPIView):
    """View for listing and creating courses"""
    serializer_class = CourseSerializer
    filterset_class = CourseFilter

    def get_permissions(self):
        # Allow anyone to list courses
        if self.request.method == "POST":
            return [IsAdminUser()]
        return []

    def get_queryset(self):
        return Course.objects.all()


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting courses"""
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    lookup_field = "id"

    def get_permissions(self):
        # Allow anyone to retrieve courses
        if self.request.method == "GET":
            return []
        return [IsAdminUser()]

    def get_queryset(self):
        return Course.objects.all()
