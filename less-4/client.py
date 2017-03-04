
import socket
from json import dumps

HOST = '192.168.0.74' #'127.0.0.1'
PORT = 50007

login = input('login:')

while True:
    message = input('new message:')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = dumps({
            'login': login,
            'message': message
        })
        s.sendall(data.encode('utf-8'))


