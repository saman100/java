from django.urls import path, reverse_lazy
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name='library'
urlpatterns = [
    path('', views.BookListView.as_view(), name='all'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('book/create',
        views.BookCreateView.as_view(success_url=reverse_lazy('library:all')), name='book_create'),
    path('book/<int:pk>/update',
        views.BookUpdateView.as_view(success_url=reverse_lazy('library:all')), name='book_update'),
    path('book/<int:pk>/delete',
        views.BookDeleteView.as_view(success_url=reverse_lazy('library:all')), name='book_delete'),

        path('index.ico', RedirectView.as_view(url=staticfiles_storage.url('images/index.ico')))
]
