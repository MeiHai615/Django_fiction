# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/11 15:58'
from django.conf.urls import url
from arts_app import views,index_handler,user_manage, details_handler
from oauth_app import views
urlpatterns = [

    url(r'^index/$', index_handler.indexHandler),
    url(r'^register/$', user_manage.register_handler, name='user_register'),
    url(r'^login/$', user_manage.login_handler, name='user_login'),
    url(r'^qq_login/$', views.qq_login, name='qq_login'),
    url(r'^logout/$', user_manage.logout_handler, name='logout'),
    url(r'^qq_check/', views.qq_check, name='qq_check'),
    url(r'^bind_email/$', views.bind_email, name='bind_email'),
    url(r'^detail/$',  details_handler.details_handler, name='detail'),
]
