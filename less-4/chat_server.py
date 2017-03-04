
import socket
from json import loads

HOST = '' #'127.0.0.1'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn: # !!!!! соединение будет автоматически закрыто
            #print('Connected by', addr)
            message = b''
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message += data

            # получаем словарь
            message = loads(message.decode('utf-8'))

            login = message.get('login')
            message = message.get('message')

            # print('login: {}'.format(login))
            # print('message: {}'.format(message))
            # print('@{login}: {message}'.format(
            #     login = login,
            #     message = message
            # ))
            print(f'@{login}: {message}')

