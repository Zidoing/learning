#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 28/12/2017.


class LinkedListUnderflow(ValueError):
    pass


class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        super(DLNode, self).__init__(elem, next_)
        self.prev = prev




bool(2)