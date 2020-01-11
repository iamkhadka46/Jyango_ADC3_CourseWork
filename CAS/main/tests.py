from django.test import TestCase
from django.urls import reverse
from main.models import Course, Teacher
from datetime import datetime
from django.contrib.auth.models import User, AbstractUser

class HeraldTest(TestCase):
    def setUp(self):
        Course.objects.create(course_title = 'Maths', course_semester = "Spring", date = datetime.now())

    def test_ORM(self):
        c1 = Course.objects.get(course_title = 'Maths')
        self.assertEqual(c1.course_title, 'Maths')

class RandomTest(TestCase):
    def setUp(self):
        Course.objects.create(course_title = 'Maths', course_semester = "Spring", date = datetime.now())

    def test_ORM(self):
        c1 = Course.objects.get(course_semester = 'Spring')
        self.assertEqual(c1.course_semester, 'Autumn')