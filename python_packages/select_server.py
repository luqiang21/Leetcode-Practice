"""
Server: handle multiple clients in parallel with select, use the select module
to manually multiplex among a set of sockets: main sockets which accept new
client connections, and input sockets connected accepted clients.
"""

import sys, time
from select import select
from socket import socket, AF_INET, SOCK_STREAM
def now(): return time.ctime(time.time())

myHost = 'localhost'             # local host
myPort = 50007
if len(sys.argv) == 3:
    myHost, myPort = sys.argv[1:]
numPortSocks = 2       # number of ports for client connects

# make main sockets for accepting new client requests
mainsocks, readsocks, writesocks = [], [], []
for i in range(numPortSocks):
    portsock = socket(AF_INET, SOCK_STREAM)
    portsock.bind((myHost, myPort))
    portsock.listen(5)
    mainsocks.append(portsock)
    readsocks.append(portsock)
    myPort += 1

# event loop: listen and multiplex until server process killed
print("select-server loop starting")
while True:
    print(readsocks)
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:        # for ready input sockets
            # port socket: accept new client
            newsock, address = sockobj.accept()
            print("Connect", address, id(newsock))
            readsocks.append(newsock)
        else:
            # client socket: read next line
            data = sockobj.recv(1024)
            print("\tgot", data.decode(), "on", id(sockobj))
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                sockobj.send(("Echo => {} at {}".format(data, now())).encode())
