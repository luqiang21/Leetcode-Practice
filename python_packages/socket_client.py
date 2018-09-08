import sys
from socket import *
serverHost = ''
serverPort = 50007

message = ['Hello network world']   # default text to send to server
if len(sys.argv) > 1:
    serverHost = sys.argv[1]        # or server from cmd line arg 1

    if len(sys.argv) > 2:           # or text from cmd line args 2..n
        message = sys.argv[2:]      # one message from each arg listed

sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP/IP socket object
sockobj.connect((serverHost, serverPort)) # connect to server machine and port

for line in message:
    sockobj.send(line.encode())
    data = sockobj.recv(1024)
    print("Client received:", repr(data))

sockobj.close()
