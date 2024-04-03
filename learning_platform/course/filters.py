"""Filters for the course Model"""

from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    NumberFilter,
)

from course.models import Course


class CourseFilter(FilterSet):

    instructor = CharFilter(lookup_expr="icontains")
    duration = NumberFilter(lookup_expr="lte")
    price = NumberFilter(lookup_expr="lte")

    class Meta:
        model = Course
        fields = [
            "instructor",
            "duration",
            "price"
        ]
