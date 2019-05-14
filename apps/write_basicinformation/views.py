from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import BasicInformationForm
from utils import restful
from .models import BasicInformation
from apps.auth_blog.models import User


@require_POST
def basic_information(request, user_id):
    form = BasicInformationForm(request.POST)
    introduction = request.POST.get('introduction')
    if form.is_valid():
        sex = form.cleaned_data.get('sex')
        age = form.cleaned_data.get('age')
        email = form.cleaned_data.get('email')
        github = form.cleaned_data.get('github')
        head_image = form.cleaned_data.get('head_image')
        User.objects.filter(uid=user_id).update(head_image=head_image)
        exists = BasicInformation.objects.filter(user_id=user_id).exists()
        if not exists:
            BasicInformation.objects.create(user_id=user_id, sex=sex, age=age, email=email, github=github,
                                            introduction=introduction, head_image=head_image)
        else:
            BasicInformation.objects.update(user_id=user_id, sex=sex, age=age, email=email, github=github,
                                            introduction=introduction, head_image=head_image)
        return restful.ok()
    else:
        return restful.params_error(message=form.errors)