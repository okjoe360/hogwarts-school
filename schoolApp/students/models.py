from django.db import models
from courses.models import CourseModel

GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('others', 'others'))
GRADES_CHOICES = (('Grade 12', 'Grade 12'), ('Grade 11', 'Grade 11'), ('Grade 10', 'Grade 10'), ('Grade 9', 'Grade 9'), ('Grade 8', 'Grade 8'))

class StudentModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES)
    grade = models.CharField(max_length=12, choices=GRADES_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Students"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

GRADE_CHOICES = (('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'))
class StudentCoursesModel(models.Model):
    student = models.ForeignKey(StudentModel, related_name='students', on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, related_name='student_courses', on_delete=models.CASCADE)
    grades = models.CharField(max_length=15, choices=GRADE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Student Courses and Grades"
        ordering = ["student", "course"]

    def __str__(self) -> str:
        return f"{self.student} | {self.course}"
