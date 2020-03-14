"""
    Pranav Bhandari
    1001551132
"""


import socket
import sys
from socket import *
import thread

def send_data( connectionSocket, addr):
    try:
        #Receiving the request
        message = connectionSocket.recv(1024)
        print "\tConnection received from {}".format(addr)
        print "\tMessage received: {}".format(message.split('\n')[0])
        filename = message.split()[1]
        if filename == "/":
            filename = "/default.html" 
        f = open(filename[1:])
        outputdata = f.read()
        # Sending one HTTP Header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        # Sending the content of the requested file to the client
        for i in range (0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except:
        # Sending response for file not found
        print "\tNo such file."
        connectionSocket.send('HTTP/1.1 404 File not found\r\n\r\n')
        connectionSocket.close()



serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
port = int(sys.argv[1]) if len(sys.argv)==2 else 8080
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
serverSocket.bind(('', port))
# Putting socket in listening mode
serverSocket.listen(5)
while True:
    #Establish Connection
    print "Ready to serve..."
    connectionSocket, addr = serverSocket.accept()
    try:
        #Starting the thread and passing the arguments to the thread.
        thread.start_new_thread(send_data, (connectionSocket, addr))
    except:
        print "Unable to start thread for address {}".format(addr)
#Closing the socket
serverSocket.close()