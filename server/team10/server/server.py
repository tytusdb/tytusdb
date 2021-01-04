import socket

import sys


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


serv_add = ('localhost', 10000)
print("hi");
serv.bind(serv_add)

serv.listen(1)

while True:
    
    print("waiting for connection")
    connection, client_address = serv.accept()

    try:
        print(client_address)
        while True:
            data = connection.recv(4096)
            print(data);
            if data:
                print("send data")
                connection.sendall(data)
            else:
                print("end data")
                break
    finally:
        connection.close()