from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from apps.cms.forms import EditArticleCategoryForm
from apps.article.models import ArticleCategory
from utils import restful


# Create your views here.
def index(request):
    return render(request, 'cms/index.html')


def write_article(request):
    return render(request, 'cms/write_article.html')


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
