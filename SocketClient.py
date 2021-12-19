import socket as SOCKET

ClientSocket = SOCKET.socket()
ClientSocket.connect(('localhost',9999))
Name = input("Enter a Name : ")
ClientSocket.send(bytes(Name,'utf-8'))
print(ClientSocket.recv(1024).decode())