import socket
import select
import sys
from event_loop import EventLoop

class Connection():
    def __init__(self):
        self.s = socket.socket()
        self.s.connect(('localhost', 1234))
    def fileno(self):
        return self.s.fileno()
    def on_read(self):
        msg = self.s.recv(1000).decode('utf8')
        print(msg)
    def send(self, msg):
        self.s.send(msg)


class Input():
    def __init__(self, sender):
        self.sender = sender
    def fileno(self):
        return sys.stdin.fileno()
    def on_read(self):
        msg = sys.stdin.readline().encode('utf8')
        self.sender.send(msg)

connection = Connection()
input_reader = Input(connection)

event_loop = EventLoop()
event_loop.add_reader(connection)
event_loop.add_reader(input_reader)
event_loop.run_forever()
