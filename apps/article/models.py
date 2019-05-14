# _*_ coding: utf-8 _*_
from django.db import models


# Create your models here.
class ArticleCategory(models.Model):
    name = models.CharField(max_length=50)
    article_num = models.IntegerField(default=0)


class Article(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    thumbnail = models.URLField()
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('ArticleCategory', on_delete=models.SET_NULL, null=True)
    user_id = models.CharField(max_length=100, null=True)

    # author = models.ForeignKey('xfzauth.User', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-pub_time']
