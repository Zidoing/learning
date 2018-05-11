#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 01/01/2018.

class StackUnderflow(ValueError): pass


class SStack(object):
    """顺序表栈"""

    def __init__(self):
        self._elem = []

    def is_empty(self):
        return self._elem == []

    def top(self):
        if self._elem == []:
            raise StackUnderflow("in top")
        return self._elem[-1]

    def push(self, elem):
        self._elem.append(elem)

    def pop(self):
        if self._elem == []:
            raise StackUnderflow("in pop")
        return self._elem.pop()


s = SStack()
s.push(3)
s.push(5)
while not s.is_empty():
    print s.pop()


class LinkedListUnderflow(ValueError):
    pass


class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack(object):
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def top(self):
        if self.top is None:
            raise StackUnderflow
        else:
            return self.top.elem

    def push(self, elem):
        self.top = LNode(elem, self.top)

    def pop(self):
        if self.top is None:
            raise StackUnderflow
        tmp = self.top
        self.top = self.top.next
        return tmp.elem



