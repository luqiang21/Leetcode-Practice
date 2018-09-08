from socket import *
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)
print("Listen on port:", myPort)

while True:
    connection, address = sockobj.accept()
    print("Server connected by", address)
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send(("Echo => " + data.decode()).encode())
    connection.close()
