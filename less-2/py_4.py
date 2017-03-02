
from abc import ABCMeta, abstractproperty, abstractclassmethod, abstractstaticmethod

class A(metaclass=ABCMeta):

    @property
    def some_prop(self):
        return 17

    @abstractproperty
    def prop(self):
        pass

    count = abstractproperty()


class B(A):

    def prop(self):
        pass

    count = 36278

print( B().some_prop )