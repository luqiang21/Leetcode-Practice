import queue, threading, time
import numpy as np


def flag():
    time.sleep(3)
    event.set()
    print("starting countdown")
    time.sleep(7)
    print("event is cleared")
    event.clear()

def start_operations():
    event.wait()
    while event.is_set():
        print("starting random integer task")
        x = np.random.randint(1, 30)
        print(x)
        time.sleep(.5)
        if x == 29:
            print("--------------True")

    print("event has been cleared, random operation stops")

event = threading.Event()
t1 = threading.Thread(target = flag)
t2 = threading.Thread(target = start_operations)
t1.start()
t2.start()
