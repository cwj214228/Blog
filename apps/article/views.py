from django.shortcuts import render
from .models import ArticleCategory, Article
from .serializers import ArticleSerializer
from utils import restful
from apps.auth_blog.models import UserShow
from django.views.decorators.http import require_POST, require_GET
# from apps.write_basicinformation.models import BasicInformation


def index(request):
    user_id = request.GET.get('user_id')
    categories = ArticleCategory.objects.all()
    articles = Article.objects.all()
    user = UserShow.objects.get(user_id=user_id)
    # user_basic_information = BasicInformation.objects.get(pk=id)

    context = {
        'categories':categories,
        'articles':articles,
        'user':user,
        # 'user_basic_information':user_basic_information
    }
    return render(request,'index.html', context=context)


def article_list(request):
    category_id = request.GET.get('category_id')
    if not category_id:
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(category_id=int(category_id))
    serializer = ArticleSerializer(articles, many=True)
    data = serializer.data
    return restful.result(data=data)


def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    try:
        back_article = Article.objects.get(pk=int(article_id) + 1)
    except:
        back_article = Article.objects.get(pk=int(article_id))

    try:
        next_article = Article.objects.get(pk=int(article_id) - 1)
    except:
        next_article = Article.objects.get(pk=int(article_id))

    context = {
        'article': article,
        'back_article': back_article,
        'next_article': next_article
    }
    return render(request, 'info.html', context=context)


