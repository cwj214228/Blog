from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import WorkExperienceForm
from .models import WorkExperience
from utils import restful


@require_POST
def work_experience(request, user_id):
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    position = request.POST.get('position')
    work_one = request.POST.get('work_one')
    work_two = request.POST.get('work_two')
    work_three = request.POST.get('work_three')
    work_four = request.POST.get('work_four')
    work_five = request.POST.get('work_five')
    work_skill_one = request.POST.get('work_skill_one')
    work_skill_two = request.POST.get('work_skill_two')
    work_skill_three = request.POST.get('work_skill_three')
    work_skill_four = request.POST.get('work_skill_four')
    work_skill_five = request.POST.get('work_skill_five')
    exists = WorkExperience.objects.filter(user_id=user_id).exists()

    try:
        if not exists:
            WorkExperience.objects.create(user_id=user_id, start_time=start_time, end_time=end_time, position=position,
                                          work_one=work_one, work_two=work_two, work_three=work_three,
                                          work_four=work_four, work_five=work_five, work_skill_one=work_skill_one,
                                          work_skill_two=work_skill_two, work_skill_three=work_skill_three,
                                          work_skill_four=work_skill_four, work_skill_five=work_skill_five)
        else:
            WorkExperience.objects.update(user=user_id, start_time=start_time, end_time=end_time, position=position,
                                          work_one=work_one, work_two=work_two, work_three=work_three,
                                          work_four=work_four, work_five=work_five, work_skill_one=work_skill_one,
                                          work_skill_two=work_skill_two, work_skill_three=work_skill_three,
                                          work_skill_four=work_skill_four, work_skill_five=work_skill_five)
        return restful.ok()
    except:
        return restful.params_error(message="数据格式错误！")
