import unittest
from django.urls import reverse
from django.test import Client
from .models import student, book, ebook
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_student(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["grade_level"] = "grade_level"
    defaults.update(**kwargs)
    return student.objects.create(**defaults)


def create_book(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["author"] = "author"
    defaults["genre"] = "genre"
    defaults.update(**kwargs)
    return book.objects.create(**defaults)


def create_ebook(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "check_out_student" not in defaults:
        defaults["check_out_student"] = create_student()
    if "book_id" not in defaults:
        defaults["book_id"] = create_book()
    return ebook.objects.create(**defaults)


class studentViewTest(unittest.TestCase):
    '''
    Tests for student
    '''
    def setUp(self):
        self.client = Client()

    def test_list_student(self):
        url = reverse('fbla_admin_student_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_student(self):
        url = reverse('fbla_admin_student_create')
        data = {
            "name": "name",
            "grade_level": "grade_level",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_student(self):
        student = create_student()
        url = reverse('fbla_admin_student_detail', args=[student.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_student(self):
        student = create_student()
        data = {
            "name": "name",
            "grade_level": "grade_level",
        }
        url = reverse('fbla_admin_student_update', args=[student.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class bookViewTest(unittest.TestCase):
    '''
    Tests for book
    '''
    def setUp(self):
        self.client = Client()

    def test_list_book(self):
        url = reverse('fbla_admin_book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        url = reverse('fbla_admin_book_create')
        data = {
            "name": "name",
            "author": "author",
            "genre": "genre",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_book(self):
        book = create_book()
        url = reverse('fbla_admin_book_detail', args=[book.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_book(self):
        book = create_book()
        data = {
            "name": "name",
            "author": "author",
            "genre": "genre",
        }
        url = reverse('fbla_admin_book_update', args=[book.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ebookViewTest(unittest.TestCase):
    '''
    Tests for ebook
    '''
    def setUp(self):
        self.client = Client()

    def test_list_ebook(self):
        url = reverse('fbla_admin_ebook_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_ebook(self):
        url = reverse('fbla_admin_ebook_create')
        data = {
            "name": "name",
            "check_out_student": create_student().pk,
            "book_id": create_book().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_ebook(self):
        ebook = create_ebook()
        url = reverse('fbla_admin_ebook_detail', args=[ebook.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_ebook(self):
        ebook = create_ebook()
        data = {
            "name": "name",
            "check_out_student": create_student().pk,
            "book_id": create_book().pk,
        }
        url = reverse('fbla_admin_ebook_update', args=[ebook.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


