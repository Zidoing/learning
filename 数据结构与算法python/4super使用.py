#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 26/12/2017.

class C1(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        print (self.x, self.y)


class C2(C1):
    def m1(self):
        super(C2,self).m1()
        print("some special service")





c = C2(1,2)
c.m1()