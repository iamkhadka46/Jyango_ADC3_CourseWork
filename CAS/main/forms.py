from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Assignment, UploadFile

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
        model = UploadFile
        fields = ('title', 'courses', 'file',)
