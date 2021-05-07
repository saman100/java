from django.test import TestCase,Client
from django.urls import reverse
from library.models import Book
import json
class TestView(TestCase):
    def setUp(self):
        self.client=Client()
        self.list_url=reverse('library:all')
    def test_Book_list_Get(self):
        response=self.client.get(self.list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'library/book_list.html')