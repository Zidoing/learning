#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/01/2018.


class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


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


class HTNode(BinTNode):
    def __lt__(self, other):
        return self.data < other.data


class HuffmanPrioQ(PrioQue):
    def number(self):
        return len(self._elems)


def HffmanTree(weights):
    """哈弗曼树     通过优先队列生成树， 然后排除2个最小值，将2个最小值组成一个新树，入队列 依次循环剩下最后一个，就是该树的顶端的顶端"""
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))

    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(x, t1, t2)
    return trees.dequeue()
