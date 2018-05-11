# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 12/02/2018.




import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)

print(list(d.items())
)

print(d)

print(d.get("fdas"))
print(d['fdsa'])

