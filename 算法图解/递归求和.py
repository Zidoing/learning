#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 17/08/2017.


input = [2, 4, 6]


def dedai(input):
    if len(input) == 1:
        return input[0]
    elif len(input) == 0:
        return 0
    else:
        return input[0] + dedai(input=input[1:])


print 12 == dedai(input)


def count_len(input):
    if len(input) == 1:
        return 1
    elif len(input) == 0:
        return 0
    else:
        return 1 + count_len(input=input[1:])


print count_len(input)


max_value = 0


def get_max(input, max_value):
    print max_value, input
    if len(input) == 0:
        return max_value
    else:
        if max_value < input[0]:
            max_value = input[0]
        return get_max(input=input[1:], max_value=max_value)


# print get_max([1, 3, 4, 5], 0)
# print get_max([1, 3, 7, 5], 0)
print get_max([100, 3, 4000, 5], 0)
