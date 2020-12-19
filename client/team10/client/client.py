import socket
import sys


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


serv_add = ('localhost', 10000)
print ('connection to port=>', serv_add)
serv.connect(serv_add)

try:
    
    message = 'data from client'
    print(message)
    serv.sendall(message.encode('utf-8'))

    
    recibido = 0
    esperado = len(message)
    
    while recibido < esperado:
        data = serv.recv(4096)
        recibido += len(data)
        print(data);

finally:
    print("connection close")
    serv.close()