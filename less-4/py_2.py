
# Echo server program
import socket

# 80 - для интернет страничек

# 127.0.0.1 = localhost - свой внутренний адрес
# 192.168.1.10 - адрес в локальной сети
# 195.120.40.100 - в интернете ?

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # зарегистрировать себе адрес
    s.listen(1)          # запуск ожидания вх. соединений
    while True:
        conn, addr = s.accept()     # получаем следующее вх. соединение
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024) # чтение из открытого сокета
                if not data: # проверка на то, что клиент больше не шлет данные
                    break
                conn.sendall(data) # отправляет данные клиенту

