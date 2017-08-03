#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime :
# @Author   : Z LEI


class P1:  # (object):
    def foo(self):
        print 'called p1 foo()'


class P2:
    def foo(self):
        print 'called p2 foo()'

    def bar(self):
        print 'called p2 bar()'


class C1(P1, P2):
    pass


class C2(P1, P2):
    def bar(self):
        print 'called c2 bar'


class GC(C1, C2):
    pass


gc = GC()
print GC.__mro__
gc.foo()
gc.bar()
