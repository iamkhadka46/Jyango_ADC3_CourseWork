from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]
   
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__" 

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = "__all__" 

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = "__all__" 

class CourseForm(forms.ModelForm):  
    class Meta:  
        model = Course  
        fields = "__all__"  