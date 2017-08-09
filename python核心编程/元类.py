#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 09/08/2017.


class C(object):
    pass


class CC:
    pass


print type(C)
print type(CC)

import types

print type(CC) is types.ClassType

from time import ctime

print '**** Welcome to Metaclasses!'
print '\t Metaclass declaration first.'


class MetaC(type):
    def __init__(cls, name, bases, attrd):
        super(MetaC, cls).__init__(name, bases, attrd)
        print "**** Created class %r at %s " % (name, ctime())


print '\t Class Foo declaration next.'


class Foo(object):
    __metaclass__ = MetaC

    def __init__(self):
        print '**** Instantiated class %r at: %s' % (self.__class__.__name__, ctime())


print '\t Class Foo instantiation next.'

f = Foo()
print '\t Done'

from warnings import warn


class ReqStrSugRepr(type):
    def __init__(self, name, bases, attrd):
        super(ReqStrSugRepr, self).__init__(name, bases, attrd)
        if '__str__' not in attrd:
            raise TypeError('class requeire overriding of __str__()')

        if '__repr__' not in attrd:
            warn('class suggest overiding of __repr__', stacklevel=3)


print '*** defined reqstrsugrepr meta class \n'


class Foo(object):
    __metaclass__ = ReqStrSugRepr

    def __str__(self):
        return 'instance of class ：%s' % self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


print 'defined class foo '


class Bar(object):
    __metaclass__ = ReqStrSugRepr

    def __str__(self):
        return 'instance of class ：%s' % self.__class__.__name__


class FooBar(object):
    __metaclass__ = ReqStrSugRepr
