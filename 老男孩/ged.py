#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 27/10/2017.
from greenlet import greenlet



def atest1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def atest2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(atest1)
gr2 = greenlet(atest2)
gr1.switch()