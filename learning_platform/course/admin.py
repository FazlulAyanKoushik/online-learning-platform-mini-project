from django.contrib import admin
from course.models import Course


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = (
        "id",
        "title",
        "instructor",
        "duration",
        "price"
    )
    readonly_fields = ("id",)
    search_fields = ("id", "title", "instructor")
    list_filter = ("instructor",)
    list_per_page = 10


admin.site.register(Course, CourseAdmin)
