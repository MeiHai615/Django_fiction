# -*- coding: utf-8 -*-
__author__ = 'liangchao'
__date__ = '2018/7/19 14:39'

from arts_app.models import Ip
def handler_ip(func):
    def wrapper(request):
        regip = request.META['REMOTE_ADDR']
        print(regip, 'bbbbbbbbbbb')
        ip_addr = Ip.objects.filter(ip=regip).first()
        if not ip_addr:
            p = Ip(ip = regip)
            p.save()
        return func(request)
    return wrapper
