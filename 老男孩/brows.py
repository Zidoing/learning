#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 03/11/2017.

import socket

socket = socket.socket()
socket.bind(('localhost', 8000))
socket.listen(5)

while True:
    connection, address = socket.accept()
    buf = connection.recv(1024)
    print buf
    # connection.sendall(bytes('HTTP/1.1 201 OK\r\n\r\n'))
    connection.sendall(bytes('<h1>hello world</h1>'))
    connection.close()
