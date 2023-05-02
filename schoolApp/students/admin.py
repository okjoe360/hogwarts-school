from django.contrib import admin
from .models import StudentModel, StudentCoursesModel

admin.site.register(StudentModel)
admin.site.register(StudentCoursesModel)
