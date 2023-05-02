from django.db import models

TYPE_CHOICES = (('Core', 'Core'), ('Elective', 'Elective'), ('Others', 'Others'))
class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Courses"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.name}"