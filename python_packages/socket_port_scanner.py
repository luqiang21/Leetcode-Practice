import socket
server = 'pythonprogramming.net'

def pscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((server, port))
        del s
        return True
    except:
        return False

# scan ports 1 to 25
for p in range(1, 26):
    if pscan(p):
        print("port", p, "is open!!!!!")
    else:
        print("port", p, "is closed.")
