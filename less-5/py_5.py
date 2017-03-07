
from queue import Queue
from time import sleep
from threading import Thread

def sender(q):
    for a in range(10):
        q.put(a) # меняет объект
    q.put('###STOP###')
    #q.task_done()  # Запомнили !!! FIXME

def getter(q):
    while True:
        item = q.get() # меняет объект
        if item == '###STOP###': # идентификатор остановки
            break
        print(item)

q = Queue()

thread1 = Thread(target=sender, args=(q, ))
thread2 = Thread(target=getter, args=(q, ))
thread1.start()
thread2.start()


