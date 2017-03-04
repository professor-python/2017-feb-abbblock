# Echo client program
import socket

HOST = '127.0.0.1'        # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))         # соединиться с сервером
    s.sendall(b'vbfhdjbvhfjdv')      # модуль работает с байтами
    data = s.recv(1024)

print('Received: {}'.format(data.decode('utf-8')))
#print('Received', repr(data))