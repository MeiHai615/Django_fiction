# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/11 16:27'

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
def indexHandler(request):

    return render(request, 'index_handler.html')
