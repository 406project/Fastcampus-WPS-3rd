import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from member.apis import facebook

__all__ = [
    'friends_ranking',
]


def friends_ranking(request):
    if request.GET.get('error'):
        return HttpResponse('사용자 로그인 거부')
    if request.GET.get('code'):
        redirect_url = 'http://{host}{url}'.format(
            host=request.META['HTTP_HOST'],
            url=reverse('sns:friends_ranking')
        )
        print('redirect_url : %s' % redirect_url)
        code = request.GET.get('code')
        access_token = facebook.get_access_token(code, redirect_url)
        return HttpResponse('%s<br>%s' % (redirect_url, access_token))