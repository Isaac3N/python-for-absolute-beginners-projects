#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 10240
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection......')
    tcpCliSock, addr = tcpSerSock.accept()
    print('......connected from:',addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        dataB = bytes(data)
        if not dataB:
            break
        tcpCliSock.send('[%s] %s' %(
            bytes(ctime(), 'utf-8'), dataB))

    tcpCliSock.close()
tcpSerSock.close()


