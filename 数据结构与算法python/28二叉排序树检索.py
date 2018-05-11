#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/01/2018.

class Assoc(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


def bt_search(btree, key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key == entry:
            return bt.data
        elif key > entry:
            bt = bt.right
        else:
            bt = bt.left
    return None


class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


class DictBinTree(object):
    """二叉排序树 类实现"""

    def __init__(self):
        self.root = None

    def is_empty(self):
        return not self.root

    def search(self, key):
        bt = self.root
        while bt is not None:
            entry = bt.data
            if key == entry.key:
                return entry.value
            elif key > entry.key:
                bt = bt.right
            else:
                bt = bt.left
        return None

    def insert(self, key, value):
        bt = self.root
        if bt is None:
            self.root = BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                bt = bt.data.value = value
                return

    def values(self):
        """中序遍历求值"""
        t, s = self.root, []
        while t is not None or len(s) > 0:
            while t is not None:
                s.append(t)
                t = t.left
            t = s.pop()
            yield t.data.value
            t = t.right

    def delete(self, key):
        p , q = None, self.root
        while q is not None and q.data.key != key:
            p= q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None:    #  树中没有关键吗
                return

        if q.left is None:
            if p is None:
                self.root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return
