
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages #to display messages in admin panel
from .models import *
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .filters import UserFilter
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, admin_only, allowed_users
import json 



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


def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list) #using django filter plugin
    return render(request, 'main/user_list.html', {'filter': user_filter})


def assignment_list(request):
    assignments = Assignment.objects.all()
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
        assignments = Assignment.objects.filter(
            Q(course__course_title__icontains=q) |
            Q(teacher__user__first_name__icontains=q)  #using 'or' to add course to the query
        )

        for assignment in assignments:
            queryset.append(assignment) #using append to store the query
    return list(set(queryset))

def get_data_queryset1(query = None):
    queryset1 = []
    queries1 = query.split(" ")
    for s in queries1:
        submissions = Submission.objects.filter(
            Q(course__course_title__icontains=s) |
            Q(teacher__user__first_name__icontains=s) |
            Q(student__user__first_name__icontains=s)  #using 'or' to add course to the query
        )

        for submission in submissions:
            queryset1.append(submission) #using append to store the query

    return list(set(queryset1))

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher'])
def delete_assignment(request, pk): #calling object by primary key.(slug method)
    if request.method == 'POST':
        assignment = Assignment.objects.get(pk=pk)
        assignment.delete()
    return redirect('main:assignment_list')

def submission_list(request):
    submissions = Submission.objects.all()
    if request.GET:
        queryy = request.GET['s'] #for search query
        submissions = get_data_queryset1(str(queryy)) 
    return render(request, 'main/submission_list.html', {
        'submissions': submissions
    })

def grades(request):
    grades = Grade.objects.all()
    return render(request, 'main/grades.html', {
        'grades': grades
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def upload_submission(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:submission_list')
    else:
        form = SubmissionForm()
    return render(request, 'main/upload_submission.html', {
        'form': form
    })

@login_required(login_url='login')
@admin_only
def delete_submission(request, pk): #calling object by primary key.(slug method)
    if request.method == 'POST':
        submission = Submission.objects.get(pk=pk)
        submission.delete()
    return redirect('main:submission_list')

@login_required(login_url='login')
@admin_only
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

@login_required(login_url='login')
@admin_only
def show(request):  
    courses = Course.objects.all()  
    return render(request,"main/show.html",{'courses':courses})  

@login_required(login_url='login')
@admin_only
def edit(request, id):  
    course = Course.objects.get(id=id)  
    return render(request,'main/edit.html', {'course':course})  

@login_required(login_url='login')
@admin_only
def update(request, id):  
    course = Course.objects.get(id=id)  
    form = CourseForm(request.POST, instance = course)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'main/edit.html', {'course':course})  

@login_required(login_url='login')
@admin_only    
def delete(request, id):  
    course = Course.objects.get(id=id)  
    course.delete()  
    return redirect("/show")  

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher'])
def upload_grades(request):
    if request.method == 'POST':
        form = GradeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:grades')
    else:
        form = GradeForm()
    return render(request, 'main/upload_grades.html', {
        'form': form
    })
#@login_required(login_url='login')
#@allowed_users(allowed_roles=['Teacher']