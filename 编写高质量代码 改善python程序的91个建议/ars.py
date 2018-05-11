# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 02/04/2018.


import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--ouput")
args = parser.parse_args()
print args


def foo():
    a = 1

    def bar():
        b = a * 2
        print b

    return bar


print foo()()


B = type("x" ,(object,),{"value":2})

a = B()

