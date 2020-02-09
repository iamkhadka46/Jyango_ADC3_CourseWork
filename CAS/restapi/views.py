
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Course


@csrf_exempt
def api_data(request):
    course = Course.objects.all() #calling course object
    if request.method == "GET":
        dict_type = {"courses": list(course.values("course_title", "course_semester"))} #converting to json
        return JsonResponse(dict_type)

@csrf_exempt
def update_api_data(request, pk):
    course = Course.objects.get(pk = pk)
    if request.method == "GET":
        return JsonResponse({"course_title": course.course_title, "semester_title": course.course_semester})

    else:
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        course.course_title = update_data['course_title']
        course.course_semester = update_data['course_semester']
        course.save()
        return JsonResponse({'message': 'Succesfully Completed'})