
# Шаблон "Наблюдатель"

from abc import ABCMeta, abstractmethod

class PrintBase(metaclass=ABCMeta):

    @abstractmethod
    def update(self, message):
        pass

class Logger(PrintBase):

    def update(self, message):
        with open('erros.log', 'a') as f:
            f.write(message + '\n')

class Printer(PrintBase):

    def update(self, message):
        print(message)


class MessageControl:

    def __init__(self):
        self.printers = []

    def register(self, print_base): # print_base - observer
        self.printers.append(print_base)

    def notify_printers(self, message: str) -> None:
        for p in self.printers:
            p.update(message)


if __name__=='__main__':
    mc = MessageControl()
    mc.register(Logger())
    mc.register(Printer())

    mc.notify_printers('Hello all!')
    mc.notify_printers('Some other info...')