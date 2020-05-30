from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from users.models import Student
from django import forms


class CreateStudentForm(UserCreationForm):
    student_id = forms.CharField(max_length=6,min_length=6, required=True, help_text='Required. Add a valid student id')
    class Meta:
        model       = Student
        fields      = ['username','student_id','password1','password2']

class AddBio(forms.ModelForm):
    
    class Meta:
        model       = Student
        fields      = ['bio']