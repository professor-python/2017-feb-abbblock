
# multiprocessing
# - библиотека/обертка
# - позволяет раскидывать код python по процессам
from time import sleep
from multiprocessing import Process, Queue #, ? SharedMemory

GGGGG = True # разные в разных процессах

def some_func(q):
    print(q.get())
    sleep(5)
    print('END of child process')

if __name__=='__main__':
    q = Queue()
    p = Process(target=some_func, args=(q,))
    p.start()

    q.put('!!!!!!!')

    #p.daemon = True # все это у него тоже есть
    p.join()
    print('END of main process')
