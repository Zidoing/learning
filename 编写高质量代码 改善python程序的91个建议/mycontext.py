#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 02/04/2018.

class MyContextManager(object):
    def __enter__(self):
        print "entering ..."

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "leaving ..."

        if exc_type is None:
            print "no exceptions!"
            return False

        elif exc_type is ValueError:
            print "value error"
            return True
        else:

            print "other error"

            return True


with MyContextManager():
    print "test"
