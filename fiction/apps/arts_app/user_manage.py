# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/11 19:01'
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from arts_app.forms import ArtsuserRegForm, LoginForm
from fiction.utils import flash
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from arts_app.models import ArtsUser
from arts_app import index_handler
from fiction.settings import r
from django.http import JsonResponse
from captcha.models import CaptchaStore


def create_pwd_md5(str_pwd):
    import hashlib
    h1 = hashlib.md5()
    h1.update(str_pwd.encode(encoding="utf-8"))
    return h1.hexdigest()


@csrf_exempt
def register_handler(request):
    userform = ArtsuserRegForm
    if request.method == 'POST':
        userform = ArtsuserRegForm(data=request.POST)
        if not userform.is_valid():
            flash(request, 'error', f'注册失败！')
            context = dict(
                form=ArtsuserRegForm(data=request.POST)
            )

            return render(request, "register_handler.html", context=context)
        username = userform.cleaned_data['username']

        password = create_pwd_md5(userform.cleaned_data['password'])
        email = userform.cleaned_data['email']
        art_user = ArtsUser(username=username, password=password, email=email)
        r.hset('user_info', 'name', username)
        ret = r.hgetall('user_info')
        # print(ret,'*************')
        art_user.save()
        # return HttpResponse(f"恭喜, 注册用户{username}成功！")
        flash(request, "success", f"恭喜, 注册用户{username}成功！")
        return redirect(reverse(login_handler))
    context = dict(
        form=userform
    )
    return render(request, "register_handler.html", context=context)


@csrf_exempt
def login_handler(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if not login_form.is_valid():
            flash(request, 'error', f'验证码错误')
            context = dict(form=LoginForm())
            return render(request, 'login_handler.html', context=context)
        username = login_form.cleaned_data.get('username')
        password = create_pwd_md5(login_form.cleaned_data.get('password'))
        user = ArtsUser.objects.filter(username=username, password=password)
        user_first = user.first()
        if user_first:
            request.session['muser'] = user_first
            # return redirect(reverse(index_handler.indexHandler))
            return HttpResponseRedirect('/art/index')
        flash(request, 'error', f'用户{username}登录失败,用户名或者密码错误！')

    context = dict(form=login_form)
    return render(request, 'login_handler.html', context=context)


def logout_handler(request):
    del request.session['muser']

    return HttpResponseRedirect('/art/login')


def login_qq_handler(request):
    return HttpResponse('qq登录')
