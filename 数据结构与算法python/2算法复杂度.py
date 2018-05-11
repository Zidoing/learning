#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 23/12/2017.
import time


def test1(n):
    lst = []
    for i in range(n * 10000):
        lst = lst + [i]
    return lst


def test2(n):
    lst = []
    for i in range(n * 10000):
        lst.append(i)
    return lst


def test3(n):
    return [i for i in range(n * 10000)]


def test4(n):
    return list(range(n * 1000))


if __name__ == '__main__':
    for item in (test1, test2, test3, test4):
        start = time.time()
        item(9)
        print time.time() - start
