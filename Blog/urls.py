"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.article import views

urlpatterns = [
    path('', views.index),
    path('cms/', include('apps.cms.urls')),
    path('ueditor/', include('apps.ueditor.urls')),
    path('article/', include('apps.article.urls')),
    path('time_axis/', include('apps.time_axis.urls')),
    path('cms/login/', include('apps.auth_blog.urls')),
    path('cms/write_basicinformation/', include('apps.write_basicinformation.urls')),
    path('ueditor/', include('apps.ueditor.urls')),
    path('cms/work_experience/', include('apps.work_experience.urls')),
    path('about_me/', include('apps.about.urls')),
    path('blog_diary/', include('apps.blog_diary.urls')),
]
