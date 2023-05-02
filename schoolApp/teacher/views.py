from django.shortcuts import render, redirect, get_object_or_404
from courses.models import CourseModel
from teacher.models import TeacherModel, TeacherCoursesModel
from django.contrib import messages
from .forms import  TeacherForm, TeacherCoursesForm
from django.contrib.auth.decorators import login_required


@login_required
def teachers(request):
    template_name = 'teachers.html'
    context = {'form': TeacherForm()}
    context['breadcrumbs'] = [{'name':'Home', 'link':'/'}, {'name':'Teachers', 'link':'/teachers'}]
    context['title'] = 'Professors List'

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Professor added successfully')
        else:
            messages.error(request, 'Network error')
        return redirect('/teachers')
    else:
        context['teachers'] = TeacherModel.objects.all()
    return render(request, template_name, context)


@login_required
def manage_teachers(request, pk):
    if request.method == 'POST':
        teacher = get_object_or_404(TeacherModel, pk=request.POST.get('pk'))
        form = TeacherForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            messages.success(request, 'Professor Details Updated')
        else:
            messages.error(request, 'Network error')
    else:
        teacher = get_object_or_404(TeacherModel, pk=pk)
        teacher.delete()
        messages.success(request, 'Professor Deleted')
    return redirect('/teachers')


@login_required
def add_courses(request, pk):
    teacher = get_object_or_404(TeacherModel, pk=pk)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = get_object_or_404(CourseModel, pk=course_id)

        if course.name in [c.course.name for c in teacher.teachers.all()]:
            messages.error(request, 'Course already registered to Professor')
            return redirect('/teachers')
        TeacherCoursesModel(teacher=teacher, course=course).save()
        messages.success(request, 'Professor Courses Updated')
        return redirect('/teachers')
    else:
        courses = CourseModel.objects.all()
        context= {'teacher':teacher, 'courses':courses}
        return render(request, 'add-courses.html', context)
    
@login_required
def remove_course(request, pk):
    query = get_object_or_404(TeacherCoursesModel, pk=pk)
    query.delete()
    messages.success(request, 'Professor Courses Removed')
    return redirect('/teachers')



