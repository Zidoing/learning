#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 28/12/2017.


def list_sort(lst):
    """
    插入排序
    :param lst:
    :return:
    """
    for i in range(1, len(lst)):
        value = lst[i]
        j = i
        while value < lst[j - 1] and j > 0:
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = value
