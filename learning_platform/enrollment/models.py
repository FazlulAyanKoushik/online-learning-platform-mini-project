from django.db import models

from course.models import Course


# Create your models here.
class Enrollment(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.DO_NOTHING,
        related_name="enrollments",
    )
    student_name = models.CharField(max_length=100)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} enrolled in {self.course.title}"

    class Meta:
        verbose_name_plural = "Enrollments"
        ordering = ["-enrollment_date"]
