# Manual Tecnico

## Librerias

```python
import socket
import tkinter as tk

```
+ socket: Los sockets y el socket API se utilizan para enviar mensajes a través de una red. Proporcionan una forma de comunicación entre procesos (IPC).

+ tkinter: El paquete tkinter ("interfaz Tk") es la interfaz estándar de Python para el conjunto de herramientas de la interfaz gráfica Tk.

## Conexion

```python
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_add = ('localhost', 10000)
print('connection to port=>', serv_add)
serv.connect(serv_add)

```

+ Se crea una ocurrencia de la clase socket.socket(parametro1, parametro2), donde el parámetro 1 socket.AF_INET es el tipo de socket para la versión ipv4, y el parámetro 2 es el socket.SOCK_STREAM donde hace referencia al protocolo de conexión TCP. Al serve_add se le asigna el host y el puerto, para poder mandárselo al ser.connect y realizar la conexión.

## Metodos

```python
now = datetime.now()
format = now.strftime(
    'Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M Segundos: %S')
print(format)

```
+ Método que regresa la fecha y hora del sistema. El método datetime.now() retorna la fecha y hora unida del sistema actual, con el metodo now.strftime() se le da un formato mas legible para la fecha y hora.


```python
def f_query_tool(self):
        self.QueryTool2.pack(side = TOP, fill = X)     
        self.QueryTool.pack_forget()

```

+ Método que habilita e inhabilita un Frame, el .pack() habilita el Frame, mientras que él .pack_forget() inhabilita un Frame
