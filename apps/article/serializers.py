#encoding: utf-8

from rest_framework import serializers
from .models import Article, ArticleCategory
from apps.cms.models import Banner


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ('id','name')


class ArticleSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer()

    class Meta:
        model = Article
        fields = ('id', 'title', 'desc', 'thumbnail', 'pub_time', 'category')


# class CommentSerizlizer(serializers.ModelSerializer):
#     author = UserSerializer()
#     class Meta:
#         model = Comment
#         fields = ('id','content','author','pub_time')

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'image_url', 'priority', 'link_to')
