from django.db import models
from courses.models import CourseModel

GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('others', 'others'))

class TeacherModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Professors"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class TeacherCoursesModel(models.Model):
    teacher = models.ForeignKey(TeacherModel, related_name='teachers', on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, related_name='courses', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Professor's Courses"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.teacher} | {self.course}"
