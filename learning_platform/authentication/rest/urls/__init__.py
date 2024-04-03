from django.urls import path, include

urlpatterns = [
    path("register", include("authentication.rest.urls.registrations")),
]