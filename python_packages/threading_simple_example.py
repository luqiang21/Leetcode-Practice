import threading
import time

def sleeper(n, name):
    print("I am {}, and I am going to sleep for {} seconds.".format(name, n))

    time.sleep(n)
    print("Hi, {} is back!".format(name))

t = threading.Thread(target = sleeper, name = 'threader1', args = (1, 'threader1'))

t.start()
t.join() # to prevent running of all other threads

print("hello, I am main thread")
print("hello, I am main thread")



# multiple threads
threads_list = []
start = time.time()
for i in range(5):
    t = threading.Thread(target = sleeper, name = 'threader{}'.format(i),
                         args = (2, 'threader{}'.format(i)))
    t.start()
    print('{} has started'.format(t.name))
    threads_list.append(t)

for t in threads_list:
    t.join()

print("all five tasks finished")
print("time took: {}".format(time.time() - start))
print("----------------hello I am outside")



# no threads
start = time.time()
for i in range(5):
    print('{} has started'.format(i))
    sleeper(2, i)


print("all five tasks finished")
print("time took: {}".format(time.time() - start))
