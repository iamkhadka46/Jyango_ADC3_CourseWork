
from django.shortcuts import render, redirect
from main.models import *
from django.http import HttpResponse,JsonResponse
from main.decorators import unauthenticated_user, admin_only, allowed_users
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='login')
@admin_only  
@csrf_exempt
def api_data(request):
    course = Course.objects.all() #calling course object
    if request.method == "GET":
        dict_type = {"courses": list(course.values("course_title", "course_semester", "date"))} #converting to json
        return JsonResponse(dict_type)

@csrf_exempt
@login_required(login_url='login')
@admin_only  
def update_api_data(request, pk):
    course = Course.objects.get(pk = pk)
    if request.method == "GET":
        return JsonResponse({"course_title": course.course_title, "course_semester": course.course_semester, "date":course.date})

    elif request.method == "PUT":
        json_data = request.body.decode("utf-8")
        update_data = json.loads(json_data)
        course.course_title = update_data["course_title"]
        course.course_semester = update_data["course_semester"]
        course.date = update_data["date"]
        course.save()

        return JsonResponse({"message": "Succesfully Completed"})
    
    elif request.method == "DELETE":
        course.delete()
        return JsonResponse({"Success":"Course Successfully Deleted!!"})


@login_required(login_url='login')
@admin_only  
@csrf_exempt
def create_course(request):
    if request.method == "POST":
        json_data = request.body.decode('utf-8')#convert text to utf-8 formattiing for json
        create_course = json.loads(json_data) #load data
        course_title = create_course['course_title']
        course_semester = create_course['course_semester']
        date = create_course['date']
        course = Course.objects.create(course_title=course_title, course_semester = course_semester, date = date) #creating course object
        try:
            course.save()
            return JsonResponse({"Success":"Course has been added successfully!"})
        except:
            return JsonResponse({"Error":"Course could not be added!"})

@login_required(login_url='login')
@admin_only  
def api_assignments(request,PAGENO,SIZE): # pagination for assignment
    if request.method == "GET":
        skip = SIZE * (PAGENO -1)
        assignments = Assignment.objects.all() [skip:(PAGENO * SIZE)]
        dict_type = {"assignments": list(assignments.values("assign_file", "course", "date", "due_date", "teacher"))}
    return JsonResponse(dict_type)

@login_required(login_url='login')
@admin_only  
def api_posts(request,PAGENO,SIZE): # pagination for post
    if request.method == "GET":
        skip = SIZE * (PAGENO -1)
        posts = Post.objects.all() [skip:(PAGENO * SIZE)]
        dict_type = {"posts": list(posts.values("title", "content", "course", "date_posted"))}
    return JsonResponse(dict_type)