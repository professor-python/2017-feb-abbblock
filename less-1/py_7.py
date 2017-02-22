
# Полиморфизм в Python

1 + 2       # ----> 3
"2" + "3"   # ----> "23"


class Workers(list):
    pass

class Worker:

    # переопределение операторов
    def __add__(self, b): # в b попадает 2е слагаемое
        workers = Workers()
        workers.append(self)
        workers.append(b)
        return workers

    def __mul__(self, mnoz): # mnoz справа от *
        workers = Workers()
        for i in range(mnoz):
            workers.append(Worker())
        return workers

    def __rmul__(self, mnoz): # mnoz слева от *
        return self * mnoz

    # def __sub__(self, b): # -
    #     pass

    # def __lt__(self, b):  # <
    #     pass

    # def __le__(self, b):  # <=
    #     pass

# a + b
# a - b
# * / > < ** 

# from datetime import datetime
# datetime() + datetime()  -->  timdelta()

#         
workers = Worker() + Worker()
#print( workers, type(workers) )

print( Worker() * 10 )
print( 10 * Worker() )
