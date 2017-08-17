#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime :
# @Author   : Z LEI

class ProtectAndHideX(object):
    def __init__(self, x):
        assert isinstance(x, int), 'x must be an integer'
        self.__x = ~x

    def get_x(self):
        return ~self.__x

    x = property(get_x)


inst = ProtectAndHideX(333333)
print inst.x

from math import pi


def get_pi(dummy):
    return pi


class PI(object):
    pi = property(get_pi, )


inst = PI()

print inst.pi
