import socket, queue, threading
target = 'pythonprogramming.net'
print_lock = threading.Lock()


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn = s.connect((target, port))
        with print_lock:
            print('port', port, 'is open!')
        conn.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = queue.Queue()

for x in range(30):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker in range(1, 101):
    q.put(worker)

q.join()
