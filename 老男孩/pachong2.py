#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 15/11/2017.

import requests
from concurrent.futures import ThreadPoolExecutor

urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]


def async_url(url):
    response = requests.get(url)
    print('begin url:%s' % url)
    print(response)


def callback(futer):
    print(222)

pool = ThreadPoolExecutor(5)

for url in urls:
    a = pool.submit(async_url, url)
    a.add_done_callback(callable)

print('')


import aiohttp