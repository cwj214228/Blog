from django.db import models
from apps.auth_blog.models import User


class BasicInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sex = models.CharField(max_length=10, null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    github = models.URLField(null=True)
    head_image = models.URLField(null=True)
    introduction = models.TextField(null=True)