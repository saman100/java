from django.test import TestCase
from django.contrib.auth.models import User
from library.models import Book

class TestModel(TestCase):
    def setUp(self) :
        user=User.objects.create_user("ahmad","","zxcv1375")
        Book.objects.create(title="php",description="gooddddd",owner=user,category="a")
    def test_model_str(self):
        book=Book.objects.get(title="php")
        self.assertEquals(book.title,book.__str__())