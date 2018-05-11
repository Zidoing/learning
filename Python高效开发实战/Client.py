#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 19/02/2018.


import socket


s  = socket.socket()

s.connect(("127.0.0.1", 3434))

data = s.recv(1024)

print(data)

s.close()
