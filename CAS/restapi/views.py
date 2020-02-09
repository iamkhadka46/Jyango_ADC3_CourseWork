

from main.models import Course
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def api_data(request):
    course = Course.objects.all() #calling course object
    if request.method == "GET":
        dict_type = {"courses": list(course.values("course_title", "course_semester", "date"))} #converting to json
        return JsonResponse(dict_type)

@csrf_exempt
def update_api_data(request, pk):
    course = Course.objects.get(pk = pk)
    if request.method == "GET":
        return JsonResponse({"course_title": course.course_title, "course_semester": course.course_semester, "date":course.date})

    else:
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        course.course_title = update_data['course_title']
        course.course_semester = update_data['course_semester']
        course.date = update_data['date']
        course.save()

        return JsonResponse({'message': 'Succesfully Completed'})

def api_assignments(request,PAGENO,SIZE): # pagination for assignment
    if request.method == "GET":
        skip = SIZE * (PAGENO -1)
        assignments = Assignment.objects.all() [skip:(PAGENO * SIZE)]
        dict_type = {"assignments": list(assignments.values("assign_file", "course", "course_id", "date", "due_date", "id", "teacher", "teacher_id"))}
    return JsonResponse(dict_type)

def api_posts(request,PAGENO,SIZE): # pagination for post
    if request.method == "GET":
        skip = SIZE * (PAGENO -1)
        posts = Post.objects.all() [skip:(PAGENO * SIZE)]
        dict_type = {"posts": list(posts.values("title", "content", "course", "date_posted"))}
    return JsonResponse(dict_type)