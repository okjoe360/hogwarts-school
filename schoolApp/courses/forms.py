from django import forms
from .models import CourseModel
 

class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        #fields = ["name", "units"]
        exclude = ['date_created']