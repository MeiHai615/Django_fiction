# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/11 15:58'
from django.conf.urls import url
from arts_app import views,index_handler,user_manage

urlpatterns = [

    url(r'^index/$', index_handler.indexHandler),
    url(r'^register/$', user_manage.register_handler, name='user_register'),

]
