#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 27/12/2017.


class LinkedListUnderflow(ValueError):
    pass


class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


q = LNode(3)


def len(head):
    p = head
    n = 0
    while p.next is not None:
        p = p.next
        n += 1
    return n


llist1 = LNode(1)
p = llist1

for i in range(2, 11):
    p.next = LNode(i)
    p = p.next

p = llist1

while p is not None:
    print p.elem
    p = p.next


class LList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        node = LNode(elem)
        node.next = self._head
        self._head = node

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            node = LNode(elem)
            self._head = node
            return
        p = self._head
        while p.next is not None:
            p = p.next
        node = LNode(elem)
        p.next = node

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow
        if self._head.next is None:
            e = self._head.elem
            self._head = None
            return e
        p = self._head
        while p.next.next is not None:
            p = p.next

        e = p.next.elem
        p.next = None
        return e


    def printall(self):
        p = self._head
        while p is not None:
            print p.elem
            if p.next is not None:
                print ','
            p = p.next
        print ''

mlist1 = LList()
for i in range(10):
    mlist1.prepend(i)

for i in range(11,20):
    mlist1.prepend(i)

mlist1.printall()

class LList1(LList):

    def __init__(self):
        super(LList1, self).__init__()
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head = LNode(elem,self._head)

    def append(self,elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            node = LNode(elem)
            self._rear.next = node
            self._rear = node
