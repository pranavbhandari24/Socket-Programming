#!/usr/bin/env python3
import sys
import socket
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
HOST = sys.argv[1]
PORT = int(sys.argv[2])
FILE = sys.argv[3]
request = "GET /" +FILE 
serverSocket.connect((HOST, PORT))
serverSocket.send(request.encode())
print('Received :')
data = serverSocket.recv(1024)
while data:
    print(data.decode())
    data = serverSocket.recv(1024)

serverSocket.close()