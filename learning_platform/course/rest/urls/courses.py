"""Urls for courses API."""

from django.urls import path

from course.rest.views.courses import (
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "",
        CourseListCreateAPIView.as_view(),
        name="course-list-create"
    ),
    path(
        "/<int:id>",
        CourseRetrieveUpdateDestroyAPIView.as_view(),
        name="course-retrieve-update-destroy"
    ),
]
