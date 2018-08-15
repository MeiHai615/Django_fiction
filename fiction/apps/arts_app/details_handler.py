# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/30 15:10'
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from arts_app.models import Chapter
from arts_app.models import Art


def details_handler(request):
    art_id = request.GET.get('id', 0)
    if art_id == 0:
        return HttpResponseRedirect('/art/index')
    # 小说详情
    art_queryset = Art.objects.get(id=art_id)
    # 小说章节
    art_capters = Chapter.objects.filter(art=art_id)

    context = dict(
        art=art_queryset,
        art_capters=art_capters,

    )

    return render(request, 'detail_handler.html', context=context)
