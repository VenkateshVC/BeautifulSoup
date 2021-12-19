import socket as SOCKET

socketHandle = SOCKET.socket(SOCKET.AF_INET,SOCKET.SOCK_STREAM)
socketHandle.connect(('www.google.com',80))

