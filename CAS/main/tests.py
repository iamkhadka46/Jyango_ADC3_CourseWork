from django.test import TestCase
from django.urls import reverse
from main.models import Course, Teacher
from django.utils import timezone
from datetime import datetime

class HeraldTest(TestCase):
    def setUp(self):
        Course.objects.create(course_title = 'Maths', course_semester = "Spring", date = datetime.now(tz=timezone.utc))

    def test_ORM(self):
        c1 = Course.objects.get(course_title = 'Maths')
        self.assertEqual(c1.course_title, 'Maths')

class RandomTest(TestCase):
    def setUp(self):
        Course.objects.create(course_title = 'Maths', course_semester = "Spring", date = datetime.now(tz=timezone.utc))

    def test_ORM(self):
        c1 = Course.objects.get(course_semester = 'Spring')
        self.assertNotEqual(c1.course_semester, 'Autumn')

class Test3(TestCase):
    def setUp(self):
        Course.objects.create(course_title = 'Physics', course_semester = "Fall", date = datetime.now(tz=timezone.utc))
        Course.objects.create(course_title = 'Maths', course_semester = "Spring", date = datetime.now(tz=timezone.utc))

    def test_ORM(self):
        c3 = Course.objects.get(course_semester = 'Fall')
        c4 = Course.objects.get(course_semester = 'Spring')
        self.assertIs(c3, c4)

class Test4(TestCase):
    def setUp(self):
        Course.objects.create(course_title = 'OOPD', course_semester = "Fall", date = datetime.now(tz=timezone.utc))
        Course.objects.create(course_title = 'Database', course_semester = "Spring", date = datetime.now(tz=timezone.utc))

    def test_ORM(self):
        c3 = Course.objects.get(course_title = 'OOPD')
        c4 = Course.objects.get(course_semester = 'Spring')
        self.assertIsNot(c3, c4)

class Test5(TestCase):
    def setUp(self):
        Course.objects.create(course_title = 'Physics', course_semester = "Fall", date = datetime.now(tz=timezone.utc))

    def test_ORM(self):
        c6 = Course.objects.get(course_semester = 'Fall')
        self.assertIsNone(c6)