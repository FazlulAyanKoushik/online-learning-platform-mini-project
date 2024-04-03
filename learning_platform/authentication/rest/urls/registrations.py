"""Urls for registration endpoints."""

from django.urls import path

from authentication.rest.views.registrations import RegistrationView

urlpatterns = [
    path("", RegistrationView.as_view(), name="register"),
]