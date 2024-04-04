from django.urls import reverse


def get_token_url():
    return reverse("token_obtain_pair")


def get_course_url():
    return reverse("course-list-create")


def get_course_detail_url(course_id):
    return reverse("course-retrieve-update-destroy", args=[course_id])