# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/11 19:46'

from django.shortcuts import HttpResponse,HttpResponseRedirect
from functools import wraps
from django.contrib import messages




'''
django后台向前端发送一个闪存消息
利用django自带的message系统发送一个闪存消息
'''
def flash(request, title, text, level='info'):
    LEVEL_MAP = {
        'info': messages.INFO,
        'debug': messages.DEBUG,
        'success': messages.SUCCESS,
        'warning': messages.WARNING,
        'error': messages.ERROR
    }
    level = LEVEL_MAP[level]
    messages.add_message(request, level, text, title)
    return HttpResponse(text)


def cheak_user_login(func):
    def __wrapper(*args,**kwargs):
        request = args[0]
        if  not request.session.has_key('muser'):
            return HttpResponseRedirect('/art/login')
        return func(*args,**kwargs)
    return __wrapper