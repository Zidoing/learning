#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 29/12/2017.

# 视频网址 https://www.bilibili.com/video/av11866460/
# 最长公共钱后缀





def match_string(t, p, pnext):
    """
    kmp 串匹配， 主函数
    :param t: 被匹配的字符出纳
    :param p: 匹配的串
    :param pnext: 最长公共前后缀表
    :return:
    """
    i, j = 0, 0
    m, n = len(p), len(t)
    while j < n and i < m:
        if p[i] == t[j] or i == -1:
            i, j = i + 1, j + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1


def get_pnext(p):
    """生成针对p中个位置i的下一检查位置表，用于kmp算法"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m  # 初始化数组
    while i < m - 1:  # 生成下一个pnext元素值
        pi = p[i]
        pk = p[k]
        if k == -1 or pi == pk:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]  # 退到更短相同前缀
    return pnext


print get_pnext('abbcabcaabbcaa')
print match_string('fdasfdaabbcabcaabbcaasss', 'abbcabcaabbcaa', get_pnext('abbcabcaabbcaa'))


def get_pnext(p):
    m = len(p)
    pnext = [-1] * m
    i = 0
    k = -1
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            k = k + 1
            i = i + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext


def match_string(t, p, pnext):
    i, j = 0, 0
    m, n = len(t), len(p)
    while j < n and i < m:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = pnext[j]
    if j == n:
        return i - j
    return -1


print get_pnext('abbcabcaabbcaa')
print match_string('fdasfdaabbcabcaabbcaasss', 'abbcabcaabbcaa', get_pnext('abbcabcaabbcaa'))
