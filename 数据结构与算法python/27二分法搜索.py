#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/01/2018.



def binSearch(lst, key):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        if key == lst[mid]:
            return mid
        elif key > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


print binSearch([1, 2, 3, 4, 5], 5)
