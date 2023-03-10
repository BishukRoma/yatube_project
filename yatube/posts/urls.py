# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'posts'),
    path('index.html', views.index, name = 'post_index'),
    path('group/<slug:slug>/', views.group_posts, name = 'group'),
    path('group_list.html', views.group_list, name = 'group_list'),
] 