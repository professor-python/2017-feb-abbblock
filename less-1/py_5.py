

# инкапсуляция

class SomeClass:
    def _private(self):
        pass
    def __private(self): # SomeClass().__SomeClass__private()
        pass
    def __getattr__(self): # возможность бОльшей защиты аттрибутов
        pass


# делегирование

class SomeAllWorker:

    def __init__(self):
        self.someSimpleWorker = SomeSimpleWorker()
        self.someHardWorker = SomeHardWorker()

    def do_some_hard_work(self):
        self.someHardWorker.execute()

    def do_some_simple_work(self):
        self.someSimpleWorker.execute()


worker = SomeAllWorker()
worker.do_some_hard_work() # на самом деле работает SomeHardWorker
worker.do_some_simple_work() # на самом деле работает SomeSimpleWorker

# шутка:
worker.someSimpleWorker = SomeMiddleWorker()
worker.do_some_simple_work() # на самом деле работает SomeMiddleWorker

# Основной плюс:
# - иметь возможность менять воркеров = настраивать систему !!!!

# полиморфизм




# наследование



