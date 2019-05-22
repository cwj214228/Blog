from django.db import models
from apps.auth_blog.models import User


class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    start_time = models.CharField(max_length=20, null=True)
    end_time = models.CharField(max_length=20, null=True)
    position = models.CharField(max_length=50, null=True)
    work_one = models.CharField(max_length=200, null=True)
    work_two = models.CharField(max_length=200, null=True)
    work_three = models.CharField(max_length=200, null=True)
    work_four = models.CharField(max_length=200, null=True)
    work_five = models.CharField(max_length=200, null=True)
    work_skill_one = models.CharField(max_length=200, null=True)
    work_skill_two = models.CharField(max_length=200, null=True)
    work_skill_three = models.CharField(max_length=200, null=True)
    work_skill_four = models.CharField(max_length=200, null=True)
    work_skill_five = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'workexperience'
