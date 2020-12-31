#!/usr/bin/env python

from socket import *
from time import ctime

HOST = 'localhost' # or 127.0.0.1
PORT = 21567
BUFSIZ = 10240
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    data_b = bytes(data, 'ascii')
    if not data:
        break
    tcpCliSock.send(data_b)
    data1 = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)

tcpCliSock.close() 

