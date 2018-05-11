#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 23/12/2017.


def fib(n):
    f1 =f2 =1
    for i in range(1,n):
        f1,f2 = f2, f2+f1
        print f1,f2

    return f2


print 'answer', fib(1)