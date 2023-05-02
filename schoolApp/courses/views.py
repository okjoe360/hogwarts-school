from django.shortcuts import render, redirect, get_object_or_404
from courses.models import CourseModel
from students.models import StudentModel
from teacher.models import TeacherModel
from django.contrib import messages
from .forms import  CourseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Login
"""
def login_user(request):
    logout(request)
    context = {"status":'failed','msg':''}
    
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            resp['status']='success'
        else:
            resp['msg'] = "Incorrect username or password"
    else:
        return render(request, 'users/login.html')
"""
#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required
def home(request):
    template_name = 'home.html'
    context = {}
    context['total_courses'] = CourseModel.objects.count()
    context['total_students'] = StudentModel.objects.count()
    context['total_teachers'] = TeacherModel.objects.count()
    context['total'] = context['total_courses']+context['total_students']+context['total_teachers']

    return render(request, template_name, context)

@login_required
def courses(request):
    template_name = 'courses.html'
    context = {'form': CourseForm()}
    context['title'] = 'Courses List'
    context['breadcrumbs'] = [{'name':'Home', 'link':'/'}, {'name':'Courses', 'link':'/courses'}]

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Course added successfully')
        else:
            messages.error(request, 'Network error')
        return redirect('/courses')
    else:
        context['courses'] = CourseModel.objects.all()
    return render(request, template_name, context)


@login_required
def manage_course(request, pk=0):
    if request.method == 'POST':
        course = get_object_or_404(CourseModel, pk=request.POST.get('pk'))
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Updated')
        else:
            messages.error(request, 'Network error')
    else:
        course = get_object_or_404(CourseModel, pk=pk)
        course.delete()
        messages.success(request, 'Course Deleted')
    return redirect('/courses')



from django.http import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

@login_required
def view_course(request, pk):
    resp = {'status':'failed'}
    course = get_object_or_404(CourseModel, pk=pk)
    teachers = [ f"{teacher['teacher__first_name']} {teacher['teacher__last_name']}" for teacher in list(course.courses.all().values('teacher__first_name', 'teacher__last_name')) ]
    students = [ f"{student['student__first_name']} {student['student__last_name']}" for student in list(course.student_courses.all().values('student__first_name', 'student__last_name')) ]
    resp['teachers'] = teachers
    resp['students'] = students
    resp['course'] = model_to_dict(course)
    resp['status'] = 'success'
    return JsonResponse(resp)
    #return HttpResponse(json.dumps(resp),content_type='application/json')