#!/usr/bin/env python
#_*_coding: utf8_*_

import socket

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect(("192.168.1.53",7777))
cliente.close()
