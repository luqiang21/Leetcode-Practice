import queue, threading, time

def putting_thread(q):
    while True:
        print("starting thread")
        time.sleep(5)
        q.put(5)
        print("put something")

q = queue.Queue()
t = threading.Thread(target = putting_thread, args = (q,), daemon = True)
t.start()

q.put(5)
print(q.get())
print("first item got")
print(q.get())
print("finished")
