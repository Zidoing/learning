#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 01/01/2018.


def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False

    if knap_rec(weight - wlist[n - 1], wlist, n - 1):
        print 'item' + str(n) + ":", wlist[n - 1]
        return True
    if knap_rec(weight, wlist, n - 1):
        return True
    else:
        return False


weight = 41
wlist = [1, 3,17, 23, 21, 321,  213432432, 34, 32,  4]
n = len(wlist)

knap_rec(weight, wlist, n)