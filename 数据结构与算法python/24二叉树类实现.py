#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/01/2018.




class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


def count_BinTNodes(t):
    """
    求二叉树节点数
    :param t:
    :return:
    """
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)


def sum_BinTNodes(t):
    """
    计算二叉树总和
    :param t:
    :return:
    """
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


def preorder(t, proc):
    """先根遍历    深度优先"""
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)


class QueueUnderflow(ValueError): pass


class SQueue(object):
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow

        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num = self._num - 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()  # 容量不够的时候增加
        self._elems[(self._num + self._head) % self._len] = e
        self._num = self._num + 1

    def __extend(self):
        """
        扩容
        :return:
        """
        old = self._len
        self._len = self._len * 2
        new_elems = [0] * self._len
        for i in range(old):
            new_elems[i] = self._elems[(self._head + i) % old]
        self._elems, self._head = new_elems, 0


def levelorder(t, proc):
    """宽度优先遍历的话   需要队列的支持   每次处理一个结点的时候，将其队列的左右分支加入队列"""
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)


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


def preorder_nonrec(t, proc):
    """先根遍历非 递归算法"""

    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            t = t.left
            s.push(t.right)
        t = s.pop()


def hougenbianli_nonrec(t, proc):
    """后跟遍历非递归算法"""
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right

        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None


# 定义一个二叉树类
class BinTree(object):

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def root(self):
        return self.root

    def leftchild(self):
        return self.root.left


    def rightchild(self):
        return self.root.right

