from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Courses"
        ordering = ["title"]
