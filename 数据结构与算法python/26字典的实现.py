#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/01/2018.



from collections import deque
import Queue
class DictList:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems
