from django.shortcuts import render
from apps.auth_blog.models import UserShow
from apps.article.models import Article

def blog_diary(request):
    user_id = request.GET.get('user_id')
    user = UserShow.objects.get(user_id=user_id)
    articles = Article.objects.filter(user_id=user_id)
    context = {
        'user': user,
        'articles': articles[0:10]
    }
    return render(request, 'list.html', context=context)
