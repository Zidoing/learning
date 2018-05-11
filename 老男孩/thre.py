#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 26/10/2017.

import threading
import time

num = 100

start = time.time()


def addNum():
    global num
    # num -= 1

    tmp = num
    time.sleep(0.001)
    num = tmp - 1


thread_list = []

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for i in thread_list:
    i.join()

print (num)

end = time.time()

print (end - start)
