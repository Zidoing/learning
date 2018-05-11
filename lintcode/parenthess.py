#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 08/01/2018.

def is_valid(s):
    start = ["(", "[", "{"]
    end = [")", "]", "}"]
    table = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in s:
        if i in start:
            stack.append(i)
        if i in end:
            if len(stack) ==0:
                return False
            en_stack = stack.pop()
            if en_stack != table[i]:
                return False
    if stack:
        return False
    return True



assert  is_valid("()") is True