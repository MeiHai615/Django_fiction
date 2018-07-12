# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/11 19:01'
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from arts_app.forms import ArtsuserRegForm
from fiction.utils import flash
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from arts_app.models import ArtsUser

def create_pwd_md5(str_pwd):
	import hashlib
	h1 = hashlib.md5()
	h1.update(str_pwd.encode(encoding="utf-8"))
	return h1.hexdigest()



@csrf_exempt
def register_handler(request):
    userform = ArtsuserRegForm
    if request.method == 'POST':
        userform =ArtsuserRegForm(data=request.POST)
        if not userform.is_valid():
            flash(request, 'error', f'注册失败！')
            context = dict(
                form= ArtsuserRegForm(data=request.POST)
            )

            return render(request, "register_handler.html", context=context)
        username = userform.cleaned_data['username']
        password = create_pwd_md5(userform.cleaned_data['password'])
        email = userform.cleaned_data['email']
        art_user = ArtsUser(username=username, password=password, email=email)
        art_user.save()
        # return HttpResponse(f"恭喜, 注册用户{username}成功！")
        flash(request, "success", f"恭喜, 注册用户{username}成功！")
        return redirect(reverse(register_handler))
    context = dict(
        form=userform
    )
    return render(request, "register_handler.html", context=context)


