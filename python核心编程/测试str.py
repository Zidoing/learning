#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime :
# @Author   : Z LEI


class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), "value must be float."
        self.value = round(val, 2)

    def __str__(self):
        return '%d' % self.value

    __repr__ = __str__


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name

    __repr__ = __str__


print RoundFloatManual(2.28)
