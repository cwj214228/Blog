from django.urls import path
from . import views

app_name = 'time_axis'
urlpatterns = [
    path('title_list/', views.title_list, name='title_list'),
]