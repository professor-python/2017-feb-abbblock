# АСИНХРОННОСТЬ
from time import sleep
from threading import Thread


def some_func(name):
    print(f'[ start_func: {name} ] start') #.format(name=name)
    sleep(3)
    print(f'[ start_func: {name} ] fin')

thread = Thread(target=some_func, args=('first',))
thread.start() # с распараллелились

thread2 = Thread(target=some_func, args=('second',))
thread2.start() # с распараллелились

print('[ main ] start')
sleep(3)
print('[ main ] fin')


