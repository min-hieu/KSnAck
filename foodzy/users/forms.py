from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):

    student_id = forms.CharField(max_length=6,min_length=6, required=True)

    class Meta:
        model = User
        fields = ['username','student_id','password1','password2']