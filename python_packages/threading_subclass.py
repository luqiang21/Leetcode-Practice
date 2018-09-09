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

# modify run()
class MyThread(threading.Thread):
    def run(self):
        print("{} has started!".format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs
        print("{} has finished.\n".format(self.getName()))

def sleeper(n, name):
    print("Hi, I am {}. going to sleep for {} seconds".format(name, n))
    time.sleep(n)
    print("{} has woken up from sleep \n".format(name))

threads_list = []
for i in range(4):
    t = MyThread(target = sleeper,
                 name = 'thread {}'.format(i+1),
                 args = (3, 'thread {}'.format(i+1)))
    t.start()
    threads_list.append(t)

for t in threads_list:
    t.join()

print("\n\n\n")
# modify __init__ and keep original __init__
class MyThread1(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(MyThread1, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style

    def run(self, *args, **kwargs):
        print("thread starting")
        super(MyThread1, self).run(*args, **kwargs)
        print("thread has ended")

def sleeper(num, style):
    print("we are sleeping for {} seconds as {}".format(num, style))
    time.sleep(num)

t = MyThread1(3, 'yellow', target = sleeper, args = [3, 'yellow'])
t.start()
