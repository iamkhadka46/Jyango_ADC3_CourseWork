from django.contrib import admin
from .models import Course, Student, Post, Teacher, Assignment, Submission, User, UploadFile
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Post)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(UploadFile)

