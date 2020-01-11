from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from . forms import RegisterForm, AssignmentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, User, UploadFile
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .filters import UserFilter


User = get_user_model()

def home_view(request):
    return render(request, 'main/home.html')

def signup_view(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        user = authenticate(username=username, password=password, email = email)
        login(request, user)
        return redirect("main:home")
    form = RegisterForm
    return render(request = request,
                  template_name = "registration/signup.html",
                  context={"form":form})

@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:home")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect('main:dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def dashboard(request):
    return render(request = request, template_name = 'main/dashboard.html', context={"courses": Course.objects.all})




class LoginView(TemplateView):
    template_name = 'main/login.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('dashboard/')
        else:
            return redirect('login/')
    return render(request, 'main/home.html')

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'main/user_list.html', {'filter': user_filter})


def assignment_list(request):
    assignments = UploadFile.objects.all()
    return render(request, 'main/assignment_list.html', {
        'assignments': assignments
    })


def upload_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'main/upload_assignment.html', {
        'form': form
    })
