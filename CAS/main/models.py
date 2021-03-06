
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.



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
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, null=True)
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
    
    def __str__(self):
        return self.due_date

class Submission(models.Model):
    sub_file = models.FileField(upload_to='Submission/')
    sub_date = models.DateField('date submitted')
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return str(self.sub_file)

class UploadFile(models.Model):
    title = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    file = models.FileField(upload_to='FilesUpload/')

class Grade(models.Model):
    submission = models.ForeignKey(Submission, on_delete = models.CASCADE, null = True)
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null = True)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null = True)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, null = True)
    grade = models.CharField(max_length = 100)




    






    
