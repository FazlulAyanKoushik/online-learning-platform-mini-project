import logging

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from course.models import Course
from course.rest.tests.url_helper import (
    get_token_url,
    get_course_url,
    get_course_detail_url,
)

logger = logging.getLogger(__name__)


class CourseAPITestCase(APITestCase):
    """Unit test for Course API"""

    def setUp(self):
        """Set up the test case."""

        self.client = APIClient()

        # Create a user
        self.user = User.objects.create_user(
            username="test_user",
            password="test_password",
            first_name="Test",
            last_name="User",
        )
        # Make the user a staff
        self.user.is_staff = True
        self.user.save()

        # Login the user
        self.user_login = self.client.post(
            get_token_url(),
            {
                "username": "test_user",
                "password": "test_password",
            },
            format="json",
        )

        # Check if the user is logged in
        self.assertEqual(self.user_login.status_code, status.HTTP_200_OK)

        # Set the authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_login.data['access']}")

    def test_create_course(self):
        """Test creating a course."""

        response = self.client.post(
            get_course_url(),
            {
                "title": "Django",
                "description": "test django description",
                "instructor": "Ayan",
                "duration": 75,
                "price": 20000.0
            },
            format="json",
        )

        # Check if the course is created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)

    def test_create_course_invalid_data_payload(self):
        """Test creating a course with invalid data payload."""

        response = self.client.post(
            get_course_url(),
            {
                "title": "Django",
                "description": "test django description",
                "instructor": "Ayan",
                "duration": 75,
            },
            format="json",
        )

        # Check if the course is not created
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Course.objects.count(), 0)

    def test_create_course_unauthorized(self):
        """Test creating a course without authorization."""

        self.client.credentials()
        response = self.client.post(
            get_course_url(),
            {
                "title": "Django",
                "description": "test django description",
                "instructor": "Ayan",
                "duration": 75,
                "price": 20000.0
            },
            format="json",
        )

        # Check if the course is not created
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Course.objects.count(), 0)

    def test_list_courses(self):
        """Test listing courses."""

        self.client.credentials()
        response = self.client.get(get_course_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 0)

        course = Course.objects.create(
            title="Django",
            description="test django description",
            instructor="Ayan",
            duration=75,
            price=20000.0
        )

        response = self.client.get(get_course_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], course.title)

    def test_retrieve_course(self):
        """Test retrieving a course."""

        self.client.credentials()
        course = Course.objects.create(
            title="Django",
            description="test django description",
            instructor="Ayan",
            duration=75,
            price=20000.0
        )

        response = self.client.get(get_course_detail_url(course.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], course.title)

    def test_update_course(self):
        """Test updating a course."""

        course = Course.objects.create(
            title="Django",
            description="test django description",
            instructor="Ayan",
            duration=75,
            price=20000.0
        )

        response = self.client.put(
            get_course_detail_url(course.id),
            {
                "title": "Django Rest Framework",
                "description": "test django rest framework description",
                "instructor": "Ayan",
                "duration": 75,
                "price": 20000.0
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django Rest Framework")

    def test_delete_course(self):
        """Test deleting a course."""

        course = Course.objects.create(
            title="Django",
            description="test django description",
            instructor="Ayan",
            duration=75,
            price=20000.0
        )

        response = self.client.delete(get_course_detail_url(course.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)
