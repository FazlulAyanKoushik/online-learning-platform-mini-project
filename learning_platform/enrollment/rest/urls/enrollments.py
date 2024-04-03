"""Urls for the enrollments API."""

from django.urls import path

from enrollment.rest.views.enrollments import (
    EnrollmentListCreateAPIView,
    EnrollmentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "",
        EnrollmentListCreateAPIView.as_view(),
        name="enrollment-list-create"
    ),
    path(
        "/<int:id>",
        EnrollmentRetrieveUpdateDestroyAPIView.as_view(),
        name="enrollment-retrieve-update-destroy"
    ),
]
