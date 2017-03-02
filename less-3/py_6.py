
# Метаклассы

# МЕТА + классы

type # -- метакласс, базовый

class SomeNewClass:
    pass

# Этот класс создает type

class SomeOtherMeclass(type):
    
    def __new__(cls, name, bases, namespace, **kwds):
        name += ' by AnimalMetaclass'
        #return super().__new__(cls, name, bases, namespace, **kwds)

        print('create class: {} bases: {} namespace: {}'.format(
            name, bases, namespace) )

        ret = type(name, bases, kwds)

        #print( namespace )

        for nm_name in namespace:
            if nm_name.startswith('__'):
                continue
            if nm_name.upper() != nm_name:
                raise Exception('''Need upper names in class {}. 

    Now you try create method '{}'.

                '''.format(name, nm_name))

        return ret

# Python 3:
class SomeOtherClass(metaclass=SomeOtherMeclass):
    
    # def some_other_method(self):
    #     pass
    def SOME_OTHER_METHOD(self):
        pass

# Python 2:
# class SomeOtherClass:
#     __metaclass__ = SomeOtherMeclass

# а это класс будет создавать SomeOtherMeclass

# Перед __init__ запускается __new__
# При создании экземпляра запускается __init__

#print( globals() )





# model.py

class SomeTable(...):

    title = StringField() # <-----
    age = IntegerField()


table = SomeTable()
title.title == 'some text' # <----- не то же самое


# Дома посмотрите в Django


