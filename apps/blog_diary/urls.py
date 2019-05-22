from django.urls import path
from . import views

app_name = 'blog_diary'
urlpatterns = [
    path('', views.blog_diary, name='blog_diary'),
]