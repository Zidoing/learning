#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 30/01/2018.

from math import hypot


class Vetcor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # def __str__(self):
    #     return 'Vector2(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vetcor(x, y)

    def __mul__(self, other):
        return Vetcor(self.x * other, self.y * other)


print(Vetcor('1', '3'))

print(Vetcor(1, 2) + Vetcor(2, 3))
print(Vetcor(1, 2) * 4)
