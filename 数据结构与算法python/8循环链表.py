#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 28/12/2017.

class LinkedListUnderflow(ValueError):
    pass


class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LCList(object):
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        if self._rear is None:
            self._rear = LNode(elem)
            self._rear.next = self._rear
        else:
            node = LNode(elem)
            node.next = self._rear.next
            self._rear.next = node

    def append(self, elem):
        if self._rear is None:
            self._rear = LNode(elem)
            self._rear.next = self._rear
        else:
            node = LNode(elem)
            node.next = self._rear.next
            self._rear.next = node
            self._rear = node

    def pop(self):  # 前端弹出
        if self._rear is None:
            raise LinkedListUnderflow
        p = self._rear.next
        if p == self._rear:
            self._rear = None
            return p.elem
        else:
            self._rear.next = p.next
            return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print (p.elem)
            if p is self._rear:
                break
            p = p.next