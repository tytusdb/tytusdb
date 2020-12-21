
# Server
+ Tiene como objetivo almacenar y transimitir peticiones del cliente desktop.
+ SO: Windows


## Librerias

```python
import socket
import sys

```

## Configuración de puerto

```python
serv_add = ('localhost', 10000)
serv.bind(serv_add)
serv.listen(1)
```


## Conexión
```python
while True:
    print("waiting for connection")
    connection, client_address = serv.accept()
```
+ serv.accept retorna la conxión y la dirección con destino hacia el cliente

```python
data = connection.recv(4096)
```
+ recv,método que nos permite recibir la data del cliente

```python
connection.sendall(data)
```
+ sendall,método que nos permite enviar data hacia el cliente

### Comando para iniciar servidor
```
python server.py
```


