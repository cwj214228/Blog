from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_GET, require_POST
from apps.cms.forms import EditArticleCategoryForm, EditArticleForm, WriteArticleForm, AddBannerForm, EditBannerForm
from apps.article.models import ArticleCategory, Article
from utils import restful
from django.views.generic import View
from django.conf import settings
from .models import Banner
import qiniu
from apps.work_experience.models import WorkExperience
from apps.write_basicinformation.models import BasicInformation
from apps.article.serializers import BannerSerializer


def login(request):
    return render(request, 'cms/login.html')


def index(request):
    if request.user.is_authenticated:
        return render(request, 'cms/cms_data.html')
    else:
        return redirect(reverse('cms:login'))


def person_message(request):
    try:
        user_message = BasicInformation.objects.get(user=request.user)
        context = {
            'user_message':user_message
        }
        return render(request, 'cms/person_message.html', context=context)
    except:
        return render(request, 'cms/person_message.html')


def work_experience(request):
    try:
        user_work = WorkExperience.objects.get(user=request.user)
        context = {
            'user_work': user_work
        }
        return render(request, 'cms/work_experience.html', context=context)
    except:
        return render(request, 'cms/work_experience.html')


@require_GET
def article_category(request):
    categories = ArticleCategory.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'cms/article_category.html', context=context)


@require_POST
def add_article_category(request):
    name = request.POST.get('name')
    exists = ArticleCategory.objects.filter(name=name).exists()
    if not exists:
        ArticleCategory.objects.create(name=name)
        return restful.ok()
    else:
        return restful.params_error(message='该分类已经存在！')


@require_POST
def delete_article_category(request):
    pk = request.POST.get('pk')
    try:
        ArticleCategory.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.unauth(message='该分类不存在！')


@require_POST
def edit_article_category(request):
    form = EditArticleCategoryForm(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get('pk')
        name = form.cleaned_data.get('name')
        try:
            ArticleCategory.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error(message='该文章分类不存在！')
    else:
        return restful.params_error(message=form.get_error())


class WriteArticleView(View):
    def get(self, request):
        categories = ArticleCategory.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'cms/write_article.html', context=context)

    def post(self, request):
        form = WriteArticleForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            category = ArticleCategory.objects.get(pk=category_id)
            Article.objects.create(title=title, desc=desc, thumbnail=thumbnail, content=content, category=category,
                                   user_id=request.user.uid)
            article_num = Article.objects.filter(category_id=category_id).count()
            ArticleCategory.objects.filter(pk=category_id).update(name=category.name, article_num=article_num)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())


class EditArticleView(View):
    def get(self, request):
        article_id = request.GET.get('article_id')
        article = Article.objects.get(pk=article_id)
        context = {
            'article': article,
            'categories': ArticleCategory.objects.all()
        }
        return render(request, 'cms/write_article.html', context=context)

    def post(self, request):
        form = EditArticleForm(request.POST)
        if form.is_valid():
            print("测试2")
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            content = form.cleaned_data.get('content')
            article_id = form.cleaned_data.get('article_id')
            category_id = form.cleaned_data.get('category')
            print(article_id)
            Article.objects.filter(id=article_id).update(title=title, desc=desc, thumbnail=thumbnail, content=content,
                                                         category=category_id)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())


@require_GET
def qntoken(request):
    access_key = settings.QINIU_ACCESS_KEY
    secret_key = settings.QINIU_SECRET_KEY
    bucket = settings.QINIU_BUCKET_NAME

    q = qiniu.Auth(access_key, secret_key)
    token = q.upload_token(bucket)
    return restful.result(data={'token': token})


@require_GET
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, "cms/artical_list.html", context=context)


@require_POST
def article_delete(request):
    article_id = request.POST.get('article_id')
    category_id = request.POST.get('category_id')
    try:
        Article.objects.filter(pk=article_id).delete()
        category = ArticleCategory.objects.get(pk=category_id)
        article_num = Article.objects.filter(category_id=category_id).count()
        ArticleCategory.objects.filter(pk=category_id).update(name=category.name, article_num=article_num)
        return restful.ok()
    except:
        return restful.params_error(message="文章不存在！")


def banners(request):
    return render(request, 'cms/banners.html')


def add_banner(request):
    form = AddBannerForm(request.POST)
    if form.is_valid():
        priority = form.cleaned_data.get('priority')
        image_url = form.cleaned_data.get('image_url')
        link_to = form.cleaned_data.get('link_to')
        banner = Banner.objects.create(priority=priority, image_url=image_url, link_to=link_to)
        return restful.result(data={"banner_id": banner.pk})
    else:
        return restful.params_error(form.get_errors())


def banner_list(request):
    banners = Banner.objects.all()
    serialize = BannerSerializer(banners, many=True)
    return restful.result(data=serialize.data)


def delete_banner(request):
    banner_id = request.POST.get('banner_id')
    Banner.objects.filter(pk=banner_id).delete()
    return restful.ok()


def edit_banner(request):
    form = EditBannerForm(request.POST)
    if form.is_valid():
        banner_id = form.cleaned_data.get('banner_id')
        priority = form.cleaned_data.get('priority')
        image_url = form.cleaned_data.get('image_url')
        link_to = form.cleaned_data.get('link_to')
        Banner.objects.filter(pk=banner_id).update(priority=priority, image_url=image_url, link_to=link_to)
        banner = Banner.objects.get(pk=banner_id)
        return restful.result(data={"banner_id": banner.pk})
    else:
        return restful.params_error(message=form.get_errors())



