from django.urls import path
from user import views

app_name='user'
urlpatterns = [
    path('post-user', views.create_user , name='create_user'),
    path('profile', views.profile , name='profile')
]