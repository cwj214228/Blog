from django.urls import path
from . import views

app_name = 'write_basicinformation'
urlpatterns = [
    path('<user_id>/', views.basic_information, name='basic_information'),

]