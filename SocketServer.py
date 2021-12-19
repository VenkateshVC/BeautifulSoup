import socket as SOCKET

serverSocket = SOCKET.socket()
serverSocket.bind(("localhost",9999))
serverSocket.listen(1)
print("Waiting For Connections ....")
CONNECTED = True
while CONNECTED:
    ServerHandle, ServerAddress = serverSocket.accept()
    Name = ServerHandle.recv(1024).decode()

    #If Name = QUIT, then close the socket and end the program.

    if Name.strip().upper() == "QUIT":
        print("Quit Entered")
        CONNECTED = False

    print("Connected with the Address: ", ServerAddress, Name)
    ServerHandle.send(bytes(("Hello World " + Name),'utf-8'))
    ServerHandle.close()



