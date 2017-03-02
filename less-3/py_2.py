from abc import ABCMeta, abstractmethod

# Фабричный метод


class MoveType(metaclass=ABCMeta):

    @abstractmethod
    def work(self):
        pass

class Fly(MoveType):

    def work(self):
         print('Лечу')

class Drive(MoveType):

    def work(self):
         print('Еду')

class Navigate(MoveType):

    def work(self):
         print('Плыву')


class Transport(metaclass=ABCMeta):

    def __init__(self):
        self.create_move_type() # экземпляр в этот момент уже существует со своим таким методом

    def work(self):
        self.move_type.work()

    @abstractmethod
    def create_move_type(self):
        pass

class Airplane(Transport):

    def create_move_type(self):
        self.move_type = Fly()

class Car(Transport):

    def create_move_type(self):
        self.move_type = Drive()

class Ship(Transport):

    def create_move_type(self):
        self.move_type = Navigate()


if __name__=='__main__':
    machine1 = Airplane()
    #machine1.create_move_type()
    machine1.work()

    machine2 = Car()
    #machine2.create_move_type()
    machine2.work()

    machine3 = Ship()
    #machine3.create_move_type()
    machine3.work()

