#Aplicación cliente 

#!/usr/bin python3

import socket

PORT = 43041  
buffer_size = 1024

print ("Introduce la dirección IP del servidor")
HOST = input ()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    print("Enviando mensaje")
    TCPClientSocket.sendall(b"Hola servidor TCP ")
    print("Esperando una respuesta")
    data = TCPClientSocket.recv(buffer_size)
    print("Recibido,", repr(data), " de", TCPClientSocket.getpeername())