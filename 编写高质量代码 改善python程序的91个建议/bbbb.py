#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 03/04/2018.

from collections import defaultdict


route_table = defaultdict(list)


def sub(self, topic, callback):
    if callback in route_table[topic]:
        return
    route_table[topic].append(callback)


def pub(self, topic, *a, **kwargs):
    for func in route_table[topic]:
        func(*a, **kwargs)


import random

def greeting(name):
    print "hello %s " .format(name)





