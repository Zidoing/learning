#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 03/01/2018.


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
