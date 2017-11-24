#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 15/11/2017.


import grequests

urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]
# 创建没有发送的request集合
rs = (grequests.get(u) for u in urls)
# 发送
print (grequests.map(rs))


# 为了防止超时和异常发生，可以指定一个异常处理器
def exception_handler(request, exception):
    print("Request failed")


reqs = [
    grequests.get('http://httpbin.org/delay/1', timeout=0.001),
    grequests.get('http://fakedomain/'),
    grequests.get('http://httpbin.org/status/500')]
grequests.map(reqs, exception_handler=exception_handler)
