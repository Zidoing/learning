#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 04/01/2018.


class PrioQueueError(ValueError):
    pass


class PrioQue(object):
    """优先队列"""

    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i > 0:
            if self._elems[i] < e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self._elems():
            raise PrioQueueError("in top")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems.pop()
