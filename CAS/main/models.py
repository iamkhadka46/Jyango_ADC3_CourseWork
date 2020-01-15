
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)


class Course(models.Model):
    course_title = models.CharField(max_length=200)
    course_semester = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.course_title

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.first_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.user.first_name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    def get_absolute_url(self):
        return reverse('post:post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Assignment(models.Model):
    date = models.DateField("date published")
    due_date = models.DateField('due date')
    assign_file = models.FileField(upload_to='Assignments/')
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    post = models.OneToOneField(Post, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.post.title



class Submission(models.Model):
    sub_file = models.FileField(upload_to='Submission/')
    sub_date = models.DateField('date submitted')
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    post = models.OneToOneField(Post, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.post.title

class UploadFile(models.Model):
    title = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    file = models.FileField(upload_to='FilesUpload/')




    






    
