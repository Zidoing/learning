#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 29/12/2017.


def naive_match(t, p):
    """

    :param t: str 源字符串
    :param p: str 被匹配的字符串
    :return:
    """
    ns, mp = len(t), len(p),
    i, j = 0, 0  # i为匹配的符合的字段长度 j 为匹配开始的地方
    while i < mp and j < ns:
        if p[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1
    if i == mp:
        return j - i
    return -1


def naive_match(string, pattern_string):
    string_len = len(string)
    pattern_len = len(pattern_string)
    count = 0
    start = 0
    while count < pattern_len and start < string_len:
        if pattern_string[count] == string[start]:
            count += 1
            start += 1
        else:
            count, start = 0, start - count + 1
    if count == pattern_len:
        return start - count
    return - 1


def match(string, other):
    len1 = len(string)
    len2 = len(other)
    length = 0
    start = 0
    while length < len2 and start < len1:
        if string[start] == other[length]:
            length, start = length + 1, start + 1
        else:
            length, start = 0, start - length + 1

    if length == len2:
        return start - length
    return -1


print naive_match('fdhgadjashgadfldghasdjlfa', 'hgadfldg')
print match('fdhgadjashgadfldghasdjlfa', 'hgadfldg')
