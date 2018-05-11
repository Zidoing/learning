#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 30/01/2018.

symbols = '&($&#@(@#$'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes = [ord(symbol) for symbol in symbols]

print(codes)

x = 'my precious'

dummy = [x for x in 'ABC']

print(x)

lax_coordinates = (33.9425, -118.408056)

import os

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City(name='Tokyo', country='JP', population=33.933, coordinates=(35.689722, 139.691667))
print(tokyo.population)

print(tokyo.coordinates)

print(tokyo[1])

print(dir(City))

print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

delhi = City._make(delhi_data)
print(delhi._asdict())
print('???')


l = list(range(10))
print(l)

l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)

l[3::2] = [11,22]
print(l)


print(dir(int))


class Person:
    aa = 1

class Student(Person):
    aa = 5

    def __init__(self):
        print(self.aa)
        print(super(Student,self).aa)


print(Student.aa)
a = Student()