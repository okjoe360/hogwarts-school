from django.shortcuts import render, redirect, get_object_or_404
from courses.models import CourseModel
from students.models import StudentModel, StudentCoursesModel
from django.contrib import messages
from .forms import  StudentForm
from django.contrib.auth.decorators import login_required

@login_required
def students(request):
    template_name = 'students.html'
    context = {'form': StudentForm()}
    context['breadcrumbs'] = [{'name':'Home', 'link':'/'}, {'name':'Students', 'link':'/students'}]
    context['title'] = 'Students List'

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Student added successfully')
        else:
            messages.error(request, 'Network error')
        return redirect('/students')
    else:
        context['students'] = StudentModel.objects.all()
    return render(request, template_name, context)


@login_required
def manage_students(request, pk):
    if request.method == 'POST':
        student = get_object_or_404(StudentModel, pk=request.POST.get('pk'))
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, 'Student Details Updated')
        else:
            messages.error(request, 'Network error')
    else:
        student = get_object_or_404(StudentModel, pk=pk)
        student.delete()
        messages.success(request, 'Student Deleted')
    return redirect('/students')


@login_required
def add_courses(request, pk):
    student = get_object_or_404(StudentModel, pk=pk)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = get_object_or_404(CourseModel, pk=course_id)

        if course.name in [c.course.name for c in student.students.all()]:
            messages.error(request, 'Course already registered to Student')
            return redirect('/students')
        StudentCoursesModel(student=student, course=course).save()
        messages.success(request, 'Student Courses Updated')
        return redirect('/students')
    else:
        courses = CourseModel.objects.all()
        context= {'student':student, 'courses':courses}
        return render(request, 'add-courses-student.html', context)
    
@login_required
def remove_course(request, pk):
    query = get_object_or_404(StudentCoursesModel, pk=pk)
    query.delete()
    messages.success(request, 'Student Courses Removed')
    return redirect('/students')

