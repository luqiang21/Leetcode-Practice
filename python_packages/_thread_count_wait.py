import _thread as thread
import time

def counter(myID, count):
    for i in range(count):
        stdoutmutex.acquire()
        # time.sleep(1)
        print(myID, "=>", i)
        stdoutmutex.release()
    exitmutexes[myID].acquire() # signal main thread

stdoutmutex = thread.allocate_lock()
exitmutexes = []
start = time.time()
for i in range(10):
    exitmutexes.append(thread.allocate_lock())
    thread.start_new(counter, (i, 3))

for mutex in exitmutexes:
    while not mutex.locked(): pass
print("main process exiting")
print("time took:", time.time() - start)
print()

# another version, simply change an integer instead of locks
exitmutexes = [0]*10
def counter(myID, count):
    for i in range(count):
        stdoutmutex.acquire()
        # time.sleep(1)
        print(myID, "=>", i)
        stdoutmutex.release()
    exitmutexes[myID] = 1 # signal main thread

stdoutmutex = thread.allocate_lock()
start = time.time()
for i in range(10):
    exitmutexes.append(thread.allocate_lock())
    thread.start_new(counter, (i, 3))

while 0 in exitmutexes: pass

print("main process exiting")
print("time took:", time.time() - start)
