import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9091

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

message = input('enter a message: ')

socket.send(message.encode('utf-8'))
print(socket.recv(1024))