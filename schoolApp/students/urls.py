from django.urls import path
from . import views

## students 
urlpatterns = [
    path('', views.students, name='students'),
    path('manage/<int:pk>/', views.manage_students, name="manage_students"),
    path('add-courses/<int:pk>/', views.add_courses, name='add_courses'),
    path('remove-course/<int:pk>/', views.remove_course, name="remove_course")
]