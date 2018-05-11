#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 25/01/2018.
import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render


def hello(request):
    print(request.path)
    print(request.get_host())
    print(request.get_full_path())
    print(request.is_secure())
    print(request.Meta)
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    html = 'It is now %s.' % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = 'It is now %s.' % dt
    return HttpResponse(html)


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request:
        message = 'you searched for : %r' % request.GET['q']
    else:
        message = 'you submitted an empty form'
    return HttpResponse(message)
