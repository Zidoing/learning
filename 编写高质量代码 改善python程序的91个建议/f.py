#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 03/04/2018.


def foo():
    sum = 0
    for i in range(10000):
        sum +=i
    return sum



if __name__ == '__main__':
    import cProfile
    cProfile.run("foo()")