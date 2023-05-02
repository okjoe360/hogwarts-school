from django import forms
from .models import StudentModel
 

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        #fields = ["name", "units"]
        exclude = ['date_created']
