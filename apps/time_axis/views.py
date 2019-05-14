from django.shortcuts import render
from apps.article.models import ArticleCategory, Article

# Create your views here.

def title_list(request):
    allArticle = Article.objects.all()
    context={
        'allArticle': allArticle
    }
    return render(request, 'time.html',context=context)
