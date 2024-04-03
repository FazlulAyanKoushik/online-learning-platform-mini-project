"""Serializers for Enrollment model."""
import re

from rest_framework import serializers

from course.models import Course
from course.rest.serializers.courses import CourseSerializer

from enrollment.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):

    course = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        required=True,
    )

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "course",
            "student_name",
            "enrollment_date",
        ]

        read_only_fields = ["id", "enrollment_date"]

    def validate_student_name(self, value):
        # Check if the student name contains any numbers or symbols
        if re.search(r'[0-9!@#$%^&*()_+={}\[\]:;"\'|<,>.?/\\]', value):
            raise serializers.ValidationError(
                "Student name must not contain numbers or symbols."
            )

        return value


class EnrollmentDetailSerializer(serializers.ModelSerializer):

    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "course",
            "student_name",
            "enrollment_date",
        ]
        read_only_fields = ["id", "enrollment_date"]
