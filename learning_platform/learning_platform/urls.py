"""
Main URL Mapping of the app.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Change Admin Top Nav Header
admin.site.site_header = "Online Learning Platform"

urlpatterns = [
    path("admin/", admin.site.urls),
    # user related urls
    path("api/v1/auth/users/", include("authentication.rest.urls")),

    # include jwt authentication
    path("api/v1/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify", TokenVerifyView.as_view(), name="token_verify"),

    # course related urls
    path("api/v1/courses", include("course.rest.urls.courses")),

    # enrollment related urls
    path("api/v1/enrollments", include("enrollment.rest.urls.enrollments")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
