#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 28/12/2017.



# 采用插入排序的方式
def sort1(self):
    """me 通过将元素进行移动"""
    head = self._head
    if head is None:
        return
    next = head.next
    while next is not None:
        next_value = next.elem
        start = head
        while start is not next and start.elem <= next_value:
            start = start.next
        while start is not next:
            start_value = start.elem
            start.elem = next_value
            start = start.next
            next_value = start_value
        next.elem = next_value
        next = next.next


def sort2(self):
    if self._head is None:
        return
    crt = self._head.next
    while crt is not None:
        x = crt.elem
        p = self._head
        while p is not crt and p.elem <= x:
            p = p.next
        while p is not crt:
            y = p.elem
            p.elem = x
            x = y
            p = p.next
        crt.elem = x
        crt = crt.next


def sort3(self):
    p = self._head
    if p is None or p.next is None:
        return
    rem = p.next
    p.next = None
    while rem is not None:
        p = self._head
        q = None
        while p is not None and p.elem <= rem.elem:
            q = p
            p = p.next
        if q is None:
            self._head = rem
        else:
            q.next = rem

        q = rem
        rem = rem.next
        q.next = p


def sort4(self):
    """me 通过将元素进行摘除"""
    p = self._head
    if p is None or p.next is None:
        return
    ano = p.next
    p.next = None
    while ano is not None:
        p = self._head
        q = None
        while p is not None and p.elem <= ano.elem:
            q = p
            p = p.next
        if q is None:
            self._head = ano
        else:
            q.next = ano

        tmp = ano
        ano = ano.next
        tmp.next = p
