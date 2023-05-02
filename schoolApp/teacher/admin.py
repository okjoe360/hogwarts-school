from django.contrib import admin
from .models import TeacherModel, TeacherCoursesModel

admin.site.register(TeacherModel)
admin.site.register(TeacherCoursesModel)
