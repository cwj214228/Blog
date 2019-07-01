from django.urls import path
from . import views

app_name = 'click_num'
urlpatterns = [
    path('', views.click_num, name='click_num'),
]