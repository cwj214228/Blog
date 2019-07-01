from django.shortcuts import render
from .models import Click_Num
from django.views.decorators.http import require_POST, require_GET
from utils import restful


@require_GET
def click_num(request):
    data = []
    num = []
    user_id = request.user.pk
    click_num = Click_Num.objects.filter(user_id=user_id).order_by('-data')[0:10:-1]
    for cnum in click_num:
        data.append(cnum.data)
        num.append(cnum.num)
    datas = {
        'data': data,
        'num': num
    }
    return restful.result(data=datas)
