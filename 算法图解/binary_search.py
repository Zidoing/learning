#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 15/08/2017.

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while (low <= high):
        mid = (low + high) / 2
        print mid
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print range(1, 101)
print binary_search(range(1, 101), 101)
