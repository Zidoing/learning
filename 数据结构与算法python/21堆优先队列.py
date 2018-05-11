#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/01/2018.


import heapq


class PrioQueueError(ValueError):
    pass


class Proqueue(object):
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if self._elems:
            self.builderheap()
        print self._elems

    def builderheap(self):
        length = len(self._elems)
        for i in range(length // 2, -1, -1):
            self.siftdown(self._elems[i], i, length)

    def siftdown(self, e, start, end):
        elems = self._elems
        i = start
        j = 2 * i + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    def is_empty(self):
        return not self._elems

    def dequeue(self):
        e = self._elems[0]
        last = self._elems.pop()
        if len(self._elems) > 0:
            self.siftdown(last, 0, len(self._elems))
        return e

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, begin):
        elems = self._elems
        i = begin
        j = (begin - 1) // 2
        while i > 0 and e < elems[i]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def sort(self):
        for i in range(len(self._elems)-1 , 0 ,-1):
            first = self._elems[0]
            last = self._elems[i]
            self._elems[i] =first
            self.siftdown(last,0,i)



heap = Proqueue([1, 2, 3, 9, 3, 54, 2])
heap.sort()
print heap._elems

while heap.is_empty() is not True:
    print heap.dequeue()


class PrioQueue(object):
    """implementing priority queues using heaps"""

    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()
        print self._elems

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)
        print self._elems

    def siftup(self, e, last):
        """
        插入一个元素后，将后续测数据都进行排序
        :param e:
        :param last:
        :return:
        """
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()  # 获取最后一个元素
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.siftdown(self._elems[i], i, end)


heap = PrioQueue([1, 2, 3, 9, 3, 54, 2])

while heap.is_empty() is not True:
    print heap.dequeue()
