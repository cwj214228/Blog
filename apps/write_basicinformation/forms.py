from django import forms
from apps.forms import FormMimin
from apps.auth_blog.models import User
from .models import BasicInformation


class BasicInformationForm(forms.Form):
    user = forms.CharField(max_length=100, error_messages={'required': '用户名必须要填写哦！'})
    sex = forms.CharField(max_length=10, error_messages={'required': '性别必须要填写哦！'})
    age = forms.CharField(max_length=20, error_messages={'required': '年龄必须要填写哦！'})
    email = forms.EmailField(error_messages={'required': 'Email也必须要填写哦！', 'invalid': "邮箱格式不对"})
    github = forms.URLField(error_messages={'required': 'Github必须要填写哦！', 'invalid': "github网址格式不对"})
    head_image = forms.URLField(error_messages={'required': '头像必须上传哦！', 'invalid': "头像网址格式不对"})
    introduction = forms.Textarea()
