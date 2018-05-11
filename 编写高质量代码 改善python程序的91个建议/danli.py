#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 02/04/2018.


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print id(s1)

print id(s2)
