#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 13/01/2018.


# 插入排序

lst = [1, 4, 2, 6, 9, 8, 3, 7, 5, 0]


def insert_sort(lst):
    """
    插入排序  把一个个元素插入到已经排序好的列表里面   复杂度平均 on2     最大on2  最小 on
    :param lst:
    :return:
    """
    for i in range(1, len(lst)):
        now = lst[i]
        j = i
        while j > 0 and lst[j - 1] > now:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = now


insert_sort(lst)
print lst


def select_order(lst):
    """
    选择排序 ， 每次都从未排序的内容里面选择一个最小的往前面放   复杂度均为on
    :param lst:
    :return:
    """
    for i in range(len(lst) - 1):
        small = i
        for j in range(i + 1, len(lst)):
            if lst[small] > lst[j]:
                small = j
        lst[small], lst[i] = lst[i], lst[small]


lst = [1, 4, 2, 6, 9, 8, 3, 7, 5, 0]
select_order(lst)
print lst


def bubule_sort(lst):
    """
    冒泡排序
    :param lst:
    :return:
    """
    for i in range(len(lst)):
        sort = True
        for j in range(1, len(lst) - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                sort = False
        if sort:
            break


lst = [1, 4, 2, 6, 9, 8, 3, 7, 5, 0]
bubule_sort(lst)
print lst


def quick_sort(lst):
    """快速排序"""
    if len(lst) < 2:
        return lst
    pos = lst[0]
    left = [i for i in lst[1:] if i <= pos]
    right = [i for i in lst[1:] if i > pos]
    return quick_sort(left) + [pos] + quick_sort(right)


lst = [1, 4, 2, 6, 9, 8, 3, 7, 5, 0]
print quick_sort(lst)

print  '------------------'


def quick_sort(lst, l, r):
    if l >= r:
        return
    i = l
    j = r
    pivot = lst[i]
    while i < j:
        while i < j and lst[j] >= pivot:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] <= pivot:
            i += 1
        if i < j:
            lst[j] = lst[i]
            j -= 1
    lst[i] = pivot
    quick_sort(lst, l, i - 1)
    quick_sort(lst, i + 1, r)


lst = [1, 4, 2, 6, 9, 8, 3, 7, 5, 0]
quick_sort(lst, 0, len(lst) - 1)
print lst


def quick_sort(lst, l, r):
    if l >= r:
        return
    i = l
    j = r
    pos = lst[i]
    while i < j:
        while i < j and lst[j] >= pos:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] <= pos:
            i += 1
        if i < j:
            lst[j] = lst[i]
    lst[j] = pos
    quick_sort(lst, l, j - 1)
    quick_sort(lst, j + 1, r)


lst = [1, 4, 2, 6, 9, 8, 3, 7, 5, 0]
quick_sort(lst, 0, len(lst) - 1)
print lst



def merge(lfrom, lto, low ,mid,high):
    i ,j , k = low , mid, low
    