from django.shortcuts import render
from apps.auth_blog.models import UserShow
from apps.write_basicinformation.models import BasicInformation
from apps.work_experience.models import WorkExperience

# Create your views here.


def about_me(request):
    user_id = request.GET.get('user_id')
    user = UserShow.objects.get(user_id=user_id)
    user_information = BasicInformation.objects.get(user_id=user_id)
    experience = WorkExperience.objects.get(user_id=user_id)
    context = {
        'user': user,
        'user_information': user_information,
        'experience': experience
    }
    return render(request, 'about.html', context=context)
