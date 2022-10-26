from http.client import ResponseNotReady
from django.shortcuts import render
from urllib import request
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from photo.models import Photo
from django.contrib.auth.mixins import AccessMixin
import requests
from datetime import datetime, timedelta

class HomeView(ListView):
    model = Photo
    template_name = 'home.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = False # 에러가 나면 메세지 / False로 바꾸면 로그인 페이지로 이동
    permission_denied_message = '작성자만이 수정 및 삭제가 가능합니다.'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

def movieAPI_TV(request):
    date = request.GET.get('date')
    if (date == '' or date is None):
        date = (datetime.today() -  timedelta(1)).strftime('%Y%m%d')
    else :
        date = date.replace('-', '')

    context = {}
    key = '41658d1753eba1594a8bd7620e0eb08f'
    url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={}&targetDt={}&itemPerPage=20'.format(key, date)

    response = requests.get(url)
    context['boxOfficeResult'] = response.json()['boxOfficeResult']
    return render(request, 'boxoffice.html', context)