import socket
from socket import *
import thread

def send_data( connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024)
        #print(message)
        filename = message.split()[1]
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
        print 'No such file.'
        connectionSocket.send('HTTP/1.1 404 File not found\r\n\r\n')
        connectionSocket.close()



serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
port = 8080
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
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    print "Connection received from {}".format(addr)
    try:
        thread.start_new_thread(send_data, (connectionSocket, addr))
    except:
        print "Unable to start thread for address {}".format(addr)
serverSocket.close()