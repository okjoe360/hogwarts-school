from django import forms
from .models import TeacherModel, TeacherCoursesModel
 

class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        #fields = ["name", "units"]
        exclude = ['date_created']

    

class TeacherCoursesForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        #fields = [course]
        exclude = ['teacher', 'date_created']