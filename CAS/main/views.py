
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from . forms import RegisterForm, AssignmentForm, CourseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages #to display messages in admin panel
from .models import Course, User, UploadFile
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .filters import UserFilter
from django.http import HttpResponse


User = get_user_model()

def home_view(request):
    return render(request, 'main/home.html')

def signup_view(request):
    form = RegisterForm(request.POST) #Calling registerform to add email field
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
    messages.info(request, "Logged out successfully!") #for django.contrib messages
    return redirect("main:home")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') #to eliminate case sensitive letter
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect('main:dashboard') #redirect to dashboard/ in urls.py
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


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:# yet to implement
            return redirect('dashboard/')
        else:
            return redirect('login/')
    return render(request, 'main/home.html')

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list) #using django filter plugin
    return render(request, 'main/user_list.html', {'filter': user_filter})


def assignment_list(request):
    assignments = UploadFile.objects.all()
    if request.GET:
        query = request.GET['q'] #for search query
        assignments = get_data_queryset(str(query)) 
    return render(request, 'main/assignment_list.html', {
        'assignments': assignments
    })

def get_data_queryset(query = None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        assignments = UploadFile.objects.filter(
            Q(title__icontains=q) |
            Q(courses__icontains=q)  #using 'or' to add course to the query
        )

        for assignment in assignments:
            queryset.append(assignment) #using append to store the query

    return list(set(queryset))

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

def delete_assignment(request, pk): #calling object by primary key.(slug method)
    if request.method == 'POST':
        assignment = UploadFile.objects.get(pk=pk)
        assignment.delete()
    return redirect('main:assignment_list')


def course(request):  
    if request.method == "POST":  
        form = CourseForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CourseForm()  
    return render(request,'main/course_list.html',{'form':form})  
def show(request):  
    courses = Course.objects.all()  
    return render(request,"main/show.html",{'courses':courses})  

def edit(request, id):  
    course = Course.objects.get(id=id)  
    return render(request,'main/edit.html', {'course':course})  

def update(request, id):  
    course = Course.objects.get(id=id)  
    form = CourseForm(request.POST, instance = course)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'main/edit.html', {'course':course})  
    
def destroy(request, id):  
    course = Course.objects.get(id=id)  
    course.delete()  
    return redirect("/show")  