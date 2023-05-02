from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('login', auth_views.LoginView.as_view(template_name = 'posApp/login.html',redirect_authenticated_user=True), name="login"),
    #path('userlogin', views.login_user, name="login-user"),
    #path('logout', views.logoutuser, name="logout"),


    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('manage-course/<int:pk>/', views.manage_course, name="manage-course"),
    path('view-course/<int:pk>/', views.view_course, name="view-course")
]