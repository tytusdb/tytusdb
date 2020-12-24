import socket 
host = "Localhost"
port = 5656
objesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objesocket.connect((host,port))
print ("Iniciando")

while True:
        enviar = input("Cliente: ")
        objesocket.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objesocket.recv (1024)
        print ("Servidor ", recibido.decode(encoding="ascii", errors="ignore"))
objesocket.close()