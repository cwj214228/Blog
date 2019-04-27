from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'cms/index.html')


def WriteArticle(request):
    return render(request, 'cms/write_article.html')

def ArticleCategory(request):
    return render(request, 'cms/article_category.html')