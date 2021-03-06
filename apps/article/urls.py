from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('list/', views.article_list, name='article_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
]