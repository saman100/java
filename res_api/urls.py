from django.urls import path
from res_api import views


app_name='res_api'
urlpatterns = [
    path('get_post_book/', views.get_post_book,name='all'),
    path('get-update-delete-book/<int:pk>', views.get_update_delete_book,name='gudb'),
    path('search-book', views.search_book)
]
