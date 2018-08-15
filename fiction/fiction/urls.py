"""fiction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import xadmin
from arts_app.views import send_message

from captcha import views

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^art/', include('arts_app.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'refresh/$', views.captcha_refresh, name='captcha-refresh'),
    url(r'^send_message/$', send_message, name='send_message'),

]
