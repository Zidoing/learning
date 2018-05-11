#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 12/02/2018.



from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)

print(dq)
