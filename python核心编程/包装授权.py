#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime :
# @Author   : Z LEI


class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return 'self.__data'

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, item):
        if item == 'nihao':
            return 'nihao'
        return getattr(self.__data, item)


wrappedComplex = WrapMe(3.5 + 4.2j)
print wrappedComplex
print wrappedComplex.real
print wrappedComplex.nihao

wrappedList = WrapMe([123, 'foo', 45.67])
wrappedList.append('bar')
print wrappedList


class SlotTedClass(object):
    __slots__ = ('foo', 'bar')


a = SlotTedClass()

a.foo = 'aa'


class AboutAttr(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print 'find me'

    def __getattribute__(self, item):
        try:
            return super(AboutAttr, self).__getattribute__(item)
        except KeyError:
            return 'default'
        except AttributeError as ex:
            print ex

    def __getattr__(self, item):
        return 'default'


at = AboutAttr('test')
print at.name
print at.not_exised


class DevNull(object):
    def __get__(self, instance, owner=None):
        print 'accessing attribute ... ignoring'
        return '1'

    def __getattribute__(self, item):
        print 'in get attribute'
        try:
            return super(DevNull, self).__getattribute__(item)
        except KeyError:
            return 'default'
        except AttributeError as ex:
            print ex

    def __set__(self, instance, value):
        print 'attempt to assign %r ... ignoring ' % value


class C1(object):
    foo = DevNull()

    def __getattribute__(self, item):
        print 'in get attribute'
        try:
            return super(C1, self).__getattribute__(item)
        except KeyError:
            return 'default'
        except AttributeError as ex:
            print ex


cl = C1()
print type(cl.foo)
cl.foo = 2
print type(cl.foo)
print cl.foo
