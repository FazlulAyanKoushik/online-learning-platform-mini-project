import logging

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from course.models import Course
from enrollment.models import Enrollment
from enrollment.rest.tests.url_helper import (
    get_token_url,
    get_enrollment_url,
    get_enrollment_detail_url,
)

logger = logging.getLogger(__name__)


class EnrollmentAPITestCase(APITestCase):
    """Unit test for Enrollment API"""

    def setUp(self):
        """Set up the test case."""

        self.client = APIClient()

        # Create a course
        self.course = Course.objects.create(
            title="Django",
            description="test django description",
            instructor="Ayan",
            duration=75,
            price=100,
        )

        # Create bulk enrollments
        self.enrollments = Enrollment.objects.bulk_create([
            Enrollment(course=self.course, student_name="Abdullah"),
            Enrollment(course=self.course, student_name="Ayan"),
        ])

    def test_create_enrollment(self):
        """Test creating an enrollment."""

        response = self.client.post(
            get_enrollment_url(),
            {
                "course": self.course.id,
                "student_name": "Abdullah"
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        enrollment_id = response.data.get("id")

        # Check if the enrollment was created
        self.assertTrue(Enrollment.objects.filter(id=enrollment_id).exists())

    def test_create_enrollment_invalid_data_payload(self):
        """Test creating an enrollment with invalid data payload."""

        response = self.client.post(
            get_enrollment_url(),
            {
                "course": self.course.id,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_enrollment_invalid_student_name(self):
        """Test creating an enrollment with invalid data payload."""

        response = self.client.post(
            get_enrollment_url(),
            {
                "course": self.course.id,
                "student_name": "1234"
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['student_name'][0],
            "Student name must not contain numbers or symbols."
        )

    def test_list_enrollments(self):
        """Test listing enrollments."""

        response = self.client.get(get_enrollment_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_retrieve_enrollment(self):
        """Test retrieving an enrollment."""

        enrollment_id = self.enrollments[0].id

        response = self.client.get(get_enrollment_detail_url(enrollment_id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], enrollment_id)


    def test_update_enrollment(self):
        """Test updating an enrollment."""

        enrollment_id = self.enrollments[0].id

        response = self.client.put(
            get_enrollment_detail_url(enrollment_id),
            {
                "course": self.course.id,
                "student_name": "Ayan"
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["student_name"], "Ayan")

    def test_delete_enrollment(self):
        """Test deleting an enrollment."""

        enrollment_id = self.enrollments[0].id

        response = self.client.delete(get_enrollment_detail_url(enrollment_id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Enrollment.objects.filter(id=enrollment_id).exists())
