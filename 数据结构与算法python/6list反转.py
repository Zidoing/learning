#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 27/12/2017.


def reverse(list):
    i = 0
    j = len(list) - 1
    while i < j:
        list[i], list[j] = list[j], list[i]
        i, j = i + 1, j - 1
