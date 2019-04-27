from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from apps.cms.forms import EditArticleCategoryForm, EditArticleForm, WriteArticleForm
from apps.article.models import ArticleCategory, Article
from utils import restful
from django.views.generic import View
from django.conf import settings
import qiniu


# Create your views here.
def index(request):
    return render(request, 'cms/index.html')


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
            Article.objects.create(title=title, desc=desc, thumbnail=thumbnail, content=content, category=category)
            return restful.ok()
        else:
            print(str(form.get_errors()))
            return restful.params_error(message=form.get_errors())


class EditArticleView(View):
    def get(self, request):
        article_id = request.GET.get('article_id')
        article = Article.objects.get(pk=article_id)
        context = {
            'artical': article,
            'categories': ArticleCategory.objects.all()
        }
        self.render = render(request, 'cms/write_article.html', context=context)
        return self.render

    def post(self, request):
        form = EditArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            pk = form.cleaned_data.get("pk")
            category = ArticleCategory.objects.get(pk=category_id)
            Article.objects.filter(pk=pk).update(title=title, desc=desc, thumbnail=thumbnail, content=content,
                                                 category=category)
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
