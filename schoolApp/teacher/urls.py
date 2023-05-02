from django.urls import path
from . import views

## teachers 
urlpatterns = [
    path('', views.teachers, name='teachers'),
    path('manage/<int:pk>/', views.manage_teachers, name="manage_teachers"),
    path('add-courses/<int:pk>/', views.add_courses, name='add_courses'),
    path('remove-course/<int:pk>/', views.remove_course, name="remove_course")
]