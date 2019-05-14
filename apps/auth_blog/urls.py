from django.urls import path
from . import views

app_name = 'auth_blog'
urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('login_data/', views.login_data, name='login_data'),
    path('img_captcha/', views.img_captcha, name='img_captcha'),
    path('sms_captcha/', views.sms_captcha, name='sms_captcha'),
    path('register/', views.register, name='register'),
    path('logout_view/', views.logout_view, name='logout_view'),
]