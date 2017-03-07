
from threading import ( Lock, RLock, Semaphore,
                        BoundedSemaphore, Thread )
from time import sleep

Lock # - простой mutex - потокобезопасный объект
     # блокировки

# a = 10

# # thread 1:
# a = 20

# # thread 2:
# a = 100

RLock # - рекурсивный mutex, один блогировщик может заблокировать многократно
Semaphore # - версия мьютекса, с ограничением по количеству блокировок
BoundedSemaphore # - версия мьютекса: кол-во блокировок == кол-во разблокировок


def sender(lst, lock):
    for a in range(10):
        lock.acquire()
        lst.append(a) # меняет объект
        lock.release()
    lock.acquire()
    lst.append('###STOP###')
    lock.release()

def getter(lst, lock):
    while True:
        if len(lst) == 0:
            sleep(0.1)
            continue
        lock.acquire()
        item = lst.pop(0) # меняет объект
        lock.release()
        if item == '###STOP###': # идентификатор остановки
            break
        print(item)

lst = []
lock = Lock()

thread1 = Thread(target=sender, args=(lst, lock))
thread2 = Thread(target=getter, args=(lst, lock))
thread1.start()
thread2.start()