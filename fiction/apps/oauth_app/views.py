from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.conf import settings
from oauth_app.oauth_clicnt import OAuth_QQ
from django.core.urlresolvers import reverse  # url逆向解析

from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.conf import settings
import time
from oauth_app.oauth_clicnt import OAuth_QQ
from oauth_app.models import OAuth_ex


# Create your views here.

def qq_login(request):
    oauth_qq = OAuth_QQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_RECALL_URL)

    # 获取 得到Authorization Code的地址
    url = oauth_qq.get_auth_url()
    # 重定向到授权页面
    return HttpResponseRedirect(url)


def qq_check(request):
    """登录之后，会跳转到这里。需要判断code和state"""
    request_code = request.GET.get('code')
    oauth_qq = OAuth_QQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_RECALL_URL)

    # 获取access_token
    access_token = oauth_qq.get_access_token(request_code)
    time.sleep(0.05)  # 稍微休息一下，避免发送urlopen的10060错误
    open_id = oauth_qq.get_open_id()
    print(open_id)
    # 检查open_id是否存在
    qqs = OAuth_ex.objects.filter(qq_openid=open_id)
    if qqs:
        # 存在则获取对应的用户，并登录
        user = qqs[0].user

        # 设置backend，绕开authenticate验证
        # setattr(user, 'backend', 'django.contrib.auth.backends.ModelBackend')
        #
        # login(request, user)
        request.session['muser'] = user
        return HttpResponseRedirect('/art/index')
    else:
        # 不存在，则跳转到绑定邮箱页面
        infos = oauth_qq.get_qq_info()  # 获取用户信息
        print(infos)
        qq_user = OAuth_ex(user=infos['nickname'], qq_openid=open_id)
        qq_user.save()
        request.session['muser'] = qq_user
        return HttpResponseRedirect('/art/index')


def bind_email(request):
    pass
