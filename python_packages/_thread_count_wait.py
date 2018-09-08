import _thread as thread

def counter(myID, count):
    for i in range(count):
        stdoutmutex.acquire()
        # time.sleep(1)
        print(myID, "=>", i)
        stdoutmutex.release()
    exitmutexes[myID].acquire() # signal main thread

stdoutmutex = thread.allocate_lock()
exitmutexes = []

for i in range(10):
    exitmutexes.append(thread.allocate_lock())
    thread.start_new(counter, (i, 3))

for mutex in exitmutexes:
    while not mutex.locked(): pass
print("main process exiting")
