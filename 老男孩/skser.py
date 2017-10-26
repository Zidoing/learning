#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 24/10/2017.


import SocketServer


class MyServer(SocketServer.BaseRequestHandler):
    pass


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 8091), MyServer)
    server.serve_forever()
