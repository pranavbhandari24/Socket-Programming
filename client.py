"""
    Pranav Bhandari
    1001551132
"""

import sys
import socket
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
#Checking the command line arguments
if len(sys.argv) <2:
    print "Please enter the correct command line arguments and try again."
    sys.exit()
#Assigning values from the command line arguments
HOST = sys.argv[1]
PORT = int(sys.argv[2]) if len(sys.argv)==3 else 8080
FILE = sys.argv[3] if len(sys.argv) ==4 else 'index.html'
request = "GET /" +FILE 

#Connecting to the HOST in the specified PORT
serverSocket.connect((HOST, PORT))
serverSocket.send(request.encode())
#Printing out the received data in chunks of 1024
print('Received :')
data = serverSocket.recv(1024)
while data:
    print(data.decode())
    data = serverSocket.recv(1024)
#Closing the socket
serverSocket.close()