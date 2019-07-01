from django.shortcuts import render
from .models import ArticleCategory, Article, Article_ReadNum
from .serializers import ArticleSerializer
from utils import restful
from apps.auth_blog.models import UserShow
from django.views.decorators.http import require_POST, require_GET
from apps.write_basicinformation.models import BasicInformation
from apps.cms.models import Banner
from apps.click_num.models import Click_Num
import time


def index(request):
    user_id = request.GET.get('user_id')
    categories = ArticleCategory.objects.all()
    articles = Article.objects.all()
    user = UserShow.objects.get(user_id=user_id)
    user_basic_information = BasicInformation.objects.get(user_id=user_id)
    banners = Banner.objects.all()
    try:
        num = Click_Num.objects.get(user_id=user_id, data=time.strftime("%Y-%m-%d", time.localtime()))
    except:
        num = Click_Num.objects.create(user_id=user_id, data=time.strftime("%Y-%m-%d", time.localtime()), num=0)

    Click_Num.objects.filter(user_id=user_id, data=time.strftime("%Y-%m-%d", time.localtime())).update(num=num.num+1)
    context = {
        'categories': categories,
        'articles': articles,
        'user': user,
        'user_basic_information': user_basic_information,
        'banners': banners,
        'toppic': articles[0:2]
    }
    return render(request, 'index.html', context=context)


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
    user_id = request.GET.get('user_id')
    articles = Article.objects.get(pk=article_id)
    user = UserShow.objects.get(user_id=user_id)

    try:
        readNum = Article_ReadNum.objects.get(user=user.user, article=articles)
    except:
        readNum = Article_ReadNum.objects.create(user=user.user, article=articles, num=1)


    try:
        back_article = Article.objects.get(pk=int(article_id) + 1)
    except:
        back_article = Article.objects.get(pk=int(article_id))

    try:
        next_article = Article.objects.get(pk=int(article_id) - 1)
    except:
        next_article = Article.objects.get(pk=int(article_id))

    context = {
        'article': articles,
        'back_article': back_article,
        'next_article': next_article,
        'user': user,
        'readNum': readNum
    }
    readNum.num += 1
    readNum.save()
    return render(request, 'info.html', context=context)


