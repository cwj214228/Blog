from django.urls import path
from . import views

app_name = 'work_experience'
urlpatterns = [
    path('<user_id>/', views.work_experience, name='work_experience'),
]