# Tytus DBMS Grupo # 08
### Cliente Desktop Linux
#### Universidad de San Carlos de Guatemala, Diciembre 2020
> Integrantes
> - Cinthya Andrea Palomo Galvez 201700670
> - Karla Julissa Ajtún Velásquez 201700565
> - Javier Alejandro Monterroso Lopez 201700831
> - Byron Antonio Orellana Alburez 201700733

# Manual de Usuario
## Pantalla Inicial
![c2492611-a0a3-4273-b2df-5aa515fc1d00](https://user-images.githubusercontent.com/14981793/102703838-cfb13b80-4239-11eb-9598-1197413e8c70.jpg)
## Editor de texto
La interfaz gráfica se compone de un editor de texto con resaltado de sintaxis sql en el cual podemos escribir consultas y nos genera la salida correspondiente en la parte inferior de la aplicación
## Arbol de Directorios
También se cuenta con un navegador en la barra lateral izquierda para poder visualizar las diferentes bases de datos a las que tenemos acceso

# Manual Técnico 
## Conexión con el servidor
se importa las clases necesarias para el funcionamiento del socket
```python
import socket
import sys
```
se utilizan dos parametros, el primero es el parametro **AF_INET** y el segundo es **SOCK_STREAM**, el primero referencia a la familia de direcciones ipv4, mientras que el segundo referencia a la protocolo de conexion TCP, por lo que se puede conectar a un servidor

```python
 try:
        conexion= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Conexion exitosamente creada")
    except socket.error as err:
        print("La creacion de la conexion fue un fracaso por: %conexion" %(err))
        #este es un puerto por defecto para el socket
    port= 80
```
Aca se puede observar la conexion, con la funcion **gethostbyname** se especifica el nombre del servidor, para conectar directamente con una direccion se utiliza la funcion **gethostbyaddr** la cual se conectara con la direccion especifica
```python
    try:
        host_ip= socket.gethostbyname('www.google.com')#conectandome con el servidor
        #PARA ENVIAR PAQUETES DE DATOS SE NECESITARA LA LIBRERIA SENDALL
    except socket.gaierror:
        print("Hubo un error en la conexion")
        sys.exit()
    conexion.connect((host_ip,port))
    print("Servidor conectado exitosamente" +str(port))
```
## Librerias
### Tkinter
Es un binding de la biblioteca gráfica Tcl/Tk para el lenguaje de programación Python. Se considera un estándar para la interfaz gráfica de usuario (GUI) para Python, para lo que se instaló:
**versión utilizada para Python 3.8.5**
```python
sudo apt-get install python3-tk
```
y se importó las librerías:
```python
import tkinter
```
### PIL
Para la instalación de las imágenes se utilizó la librería PIL

```python
from PIL import ImageTk, Image
```
para instalarlo para Python 3:

```python
python3 -m pip install Pillow
pip install Pillow
```
