
from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)


class Course(models.Model):
    course_title = models.CharField(max_length=200)
    course_semester = models.CharField(max_length=200)
    date = models.DateTimeField("date published")

    def __str__(self):
        return self.course_title

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    teacher = models.ManyToManyField(Teacher)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)

class Assignment(models.Model):
    date = models.DateField("date published")
    due_date = models.DateField('due date')
    assign_file = models.FileField(upload_to='Assignments/')
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    post = models.OneToOneField(Post, on_delete = models.CASCADE, primary_key = True)



class Submission(models.Model):
    sub_file = models.FileField(upload_to='Submission/')
    sub_date = models.DateField('date submitted')
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    post = models.OneToOneField(Post, on_delete = models.CASCADE, primary_key = True)

class UploadFile(models.Model):
    title = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    file = models.FileField(upload_to='FilesUpload/')




    






    