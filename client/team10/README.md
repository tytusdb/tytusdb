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

# Manual Usuario

## Objetivos

```
Dar a conocer cómo se utiliza la aplicación por medio de una explicación detallada.
Desarrollar una intergaz amigable al usuario.

```

## Ingreso al Sistema
+ Al iniciar la aplicacion se desplegará la siguiente ventana, en la cual deberá ingresar con usuario y contraseña.
<p align="center">
<img src="imagen/ingreso_usuario.png" width = "700" alt="ingreso al sistema">
</p>

## File
+ Abrir Archivo *.sql
Abre el archivo seleccionado en la pestaña seleccionada.
<p align="center">
<img src="imagen/abrir.png" width = "700" alt="abrir archivo *.sql">
</p>

+ Guardar Archivo *.sql
Guarda el archivo de la pestaña actual.
<p align="center">
<img src="imagen/guardar.png" width = "700" alt="guardar archivo *.sql">
</p>

## Tree View
Se desplegará una vista en forma de árbol en la cual se podrá tener acceso a las bases de datos, así como sus tablas, etc.
<p align="center">
<img src="imagen/tree.png" width = "700" alt="tree">
</p>

## Tools
+ Query Tool
Abrir un nuevo editor sql.
<p align="center">
<img src="imagen/query1.png" width = "700" alt="query1">
</p>
Se mostrará de la siguiente manera.
<p align="center">
<img src="imagen/query2.png" width = "700" alt="query2">
</p>


## Consola
Se desplegará la salida de las consultas realizadas en el editor.
<p align="center">
<img src="imagen/consola.png" width = "700" alt="console">
</p>

## About
+ Grupo 10
Se mostrarán los integrantes del grupo.
<p align="center">
<img src="imagen/integrantes.png" width = "700" alt="console">
</p>
+ TytusDB
Se abrirá el repositorio del proyecto.