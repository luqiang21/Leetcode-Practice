import queue, time
import _thread as thread

num_consumers = 2
num_producers = 4
num_messages = 4

safeprint = thread.allocate_lock()
data_queue = queue.Queue()

def producer(id_num):
    for msg_num in range(num_messages):
        time.sleep(id_num)
        data_queue.put("producer " + str(id_num) + " : " + str(msg_num))

def consumer(id_num):
    while 1:
        time.sleep(0.1)
        try:
            data = data_queue.get(block=False) # If optional args block is true
            # and timeout is None (the default), block if necessary until an item is available.
            # Otherwise (block is false), put an item on the queue if a free slot is immediately
            # available, else raise the Full exception (timeout is ignored in that case).
        except queue.Empty:
            pass
        else:                   #  must be executed if the try clause does not raise an exception
            safeprint.acquire()
            print("consumer", id_num, "got =>", data)
            safeprint.release()

if __name__ == '__main__':
    for i in range(num_consumers):
        thread.start_new(consumer, (i,))
    for i in range(num_producers):
        thread.start_new(producer, (i,))
    time.sleep(((num_producers-1) * num_messages) + 1)
