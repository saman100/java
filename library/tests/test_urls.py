from django.test import SimpleTestCase
from django.urls import resolve,reverse
from library.views import BookListView,BookCreateView

class TestUrls(SimpleTestCase):
    def test_list_url_resolve(self):
        url=reverse('library:all')
        self.assertEquals(resolve(url).func.view_class,BookListView)

    def test_add_url_resolve(self):
        url = reverse('library:book_create')
        self.assertEquals(resolve(url).func.view_class, BookCreateView)