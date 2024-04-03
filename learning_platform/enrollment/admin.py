from django.contrib import admin
from enrollment.models import Enrollment


# Register your models here.
class EnrollmentAdmin(admin.ModelAdmin):
    model = Enrollment
    list_display = (
        "id",
        "student_name",
        "course",
        "enrollment_date"
    )
    readonly_fields = ("id",)
    search_fields = ("id", "student_name", "course")
    list_filter = ("course",)
    list_per_page = 10


admin.site.register(Enrollment, EnrollmentAdmin)
