#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 28/12/2017.


def josephus_A(n, k, m):
    people = list(range(1, n + 1))
    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print "chu ju %s " % people[i]
                people[i] = 0
            i = (i + 1) % n
        if num < n - 1:
            print (",")
        else:
            print


josephus_A(16, 1, 2)
