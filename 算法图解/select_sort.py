#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 15/08/2017.


# 选择排序  找到最大的然后跟第一个换
# 默认选定一个先找到所有最小的，然后跟第一个换，然后找到剩余最小的，跟第二个换，依次类推


def select_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i, len(list)):
            print 'compare %s < %s' % (list[j], list[min_index])
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]


a = [1, 5, 6, 7, 2, 4, 9]
select_sort(a)
print a
