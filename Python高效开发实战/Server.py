#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 19/02/2018.


import socket
import datetime

HOST = '0.0.0.0'
PORT = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)


while True:
    conn, address = s.accept()
    print("Client %s connected" % str(address))
    dt = datetime.datetime.now()
    message = "current time is %s" % dt
    conn.send(bytes(message,'utf-8'))
    print(message)
    conn.close()
