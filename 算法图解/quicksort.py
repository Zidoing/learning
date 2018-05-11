#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 17/08/2017.



def quicksort(array):
    if len(array) < 2:
        return array
    else:
        jizhun = array[0]
        less = [i for i in array[1:] if i <= jizhun]
        more = [i for i in array[1:] if i > jizhun]
        return quicksort(less) + [jizhun] + quicksort(more)


print quicksort( [1, 4, 2, 6, 9, 8, 3, 7, 5, 0])
print quicksort([1,3,4,5,6,7,32,5423,4523,65,35423,5454,6534])
