
# 2 потока:

# 1 поток: по очереди животные "звучат"
# 2 поток: ждет 10 секунд и завершает (как-то?) поток 1

from abc import ABCMeta, abstractmethod
from time import sleep
from threading import Thread

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

class Duck(Animal):

    def execute(self):
        return 'KRYA-KRYA...'

class Dog(Animal):

    def execute(self):
        return 'ГАВ-ГАВ...'

class Python(Animal):

    def execute(self):
        return 'sch-sch-sch...'

STOP_VAKHANALY = False

def animals_vakhanaly(*animals):
    while not STOP_VAKHANALY:
    #for i in range(3):
        for animal in animals:
            if STOP_VAKHANALY:
                break
            print( animal.execute() )
            sleep(0.5)

thread = Thread(target=animals_vakhanaly, args=[
    Duck(),
    Dog(),
    Python()
])
#thread.daemon = True # завершится вместе с основным потоком
thread.start()


sleep(5)
STOP_VAKHANALY = True

#thread.join() # присоединиться к основному потоку

print('FIN')

# программа завершится только тогда, когда завершатся все ее потоки
