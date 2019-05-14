from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    path('', views.index, name='index'),
    path('article_category/', views.article_category, name='article_category'),
    path('add_article_category/', views.add_article_category, name='add_article_category'),
    path('delete_article_category/', views.delete_article_category, name='delete_article_category'),
    path('edit_article_category/', views.edit_article_category, name='edit_article_category'),
    path('write_article/', views.WriteArticleView.as_view(), name='write_article'),
    path('edit_article/', views.EditArticleView.as_view(), name='edit_article'),
    path('qntoken/', views.qntoken, name='qntoken'),
    path('person_message/', views.person_message, name='person_message'),
    path('work_experience/', views.work_experience, name='work_experience'),
    path('login/', views.login, name='login'),
    path('article_list/', views.article_list, name='article_list'),
    path('article_delete/', views.article_delete, name='article_delete'),
    path('banners/', views.banners, name='banners'),
    path('add_banner/', views.add_banner, name='add_banner'),
    path('banner_list/', views.banner_list, name='banner_list'),
    path('delete_banner/', views.delete_banner, name='delete_banner'),
    path('edit_banner/', views.edit_banner, name='edit_banner'),
]