
# GIL - global intepreter lock

print('Hello!') # цельная операция

for a in range(10): # 11 цельных операций
    print(a) # цельная операция

Lock # GIL - это Lock на системном уровне Python


# GIL - печалька :(
# НО:
# - multiprocessing
# - освобождать GIL --> cython

# Cython
# - переписать функцию на c и она работает быстрее
# - освобождать GIL
# - использование чужих c/c++ DLL

# module.py
def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

# setup.py
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("module.py"),  # "module.pyx"
)

# >>> python setup.py build_ext --inplace

# pyd - DLL с функциями python/cython
# - такие библиотеки можно импортировать с помощью python

# primes.py
def primes(int kmax): # <---- задали тип
    cdef int n, k, i # <---- задали тип
    cdef int p[1000] # <---- задали тип
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result


# python3 -m pip install cython