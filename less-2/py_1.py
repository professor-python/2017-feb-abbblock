
# Шаблон проектирования команда

# class Base:
    
#     def execute(self):
#         pass

class Worker(Base):

    def execute(self):
        print('work')

class Car(Base):

    def execute(self):
        print('drive')


executers = [Worker(), Car(), Car()]
for ex in executers:
    ex.execute()
