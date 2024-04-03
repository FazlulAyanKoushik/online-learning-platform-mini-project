"""Serializers for course model"""

from rest_framework import serializers

from course.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "instructor",
            "duration",
            "price",
        ]
        read_only_fields = ["id"]
