from django.shortcuts import render
from apps.article.models import ArticleCategory, Article
from apps.auth_blog.models import UserShow

# Create your views here.


def title_list(request):
    user_id = request.GET.get('user_id')
    user = UserShow.objects.get(user_id=user_id)
    allArticle = Article.objects.filter(user_id=user_id)
    context={
        'allArticle': allArticle,
        'user': user
    }
    return render(request, 'time.html', context=context)
