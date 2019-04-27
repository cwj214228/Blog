from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    path('', views.index, name='index'),
    path('write_article/', views.write_article, name='write_article'),
    path('article_category/', views.article_category, name='article_category'),
    path('add_article_category/', views.add_article_category, name='add_article_category'),
    path('delete_article_category/', views.delete_article_category, name='delete_article_category'),
    path('edit_article_category/', views.edit_article_category, name='edit_article_category'),
]