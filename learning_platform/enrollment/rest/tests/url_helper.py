from django.urls import reverse


def get_token_url():
    return reverse("token_obtain_pair")


def get_enrollment_url():
    return reverse("enrollment-list-create")


def get_enrollment_detail_url(enrollment_id):
    return reverse("enrollment-retrieve-update-destroy", args=[enrollment_id])