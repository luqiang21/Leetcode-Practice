# Threading subclassing
import os, time
import threading

class mythread(threading.Thread):       # subclass Thread object
    def __init__(self, myID, count):
        self.myID = myID
        self.count = count
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            stdoutmutex.acquire()
            print(self.myID, "=>", i)
            stdoutmutex.release()

stdoutmutex = threading.Lock()          # same as thread.allocate_lock()
threads = []
for i in range(10):
    thread = mythread(i, 3)           # make/start 10 threads
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("main thread exiting")
