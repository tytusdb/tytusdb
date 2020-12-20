import socket 
host = "Localhost"
port = 5656
Servidor  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Servidor.bind((host, port))
Servidor.listen(1)
print ("Servidor a la espera de conexion")

active, addr=Servidor.accept()

while True:
    recibido = active.recv(1024)
    print ("Cliente:", recibido.decode(encoding="ascii", errors="ignore"))
    enviar = input ("Server: " )
    active.send(enviar.encode(encoding="ascii", errors="ignore"))
active.close()