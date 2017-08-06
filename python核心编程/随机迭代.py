#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime :
# @Author   : Z LEI

from random import choice


class RandSeq(object):
    def __init__(self, seq, safe=False):
        self.iter = iter(seq)
        self.safe = safe

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval


for i in RandSeq(['one', 'two', 'three']):
    print i
